import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from torch import from_numpy
import pytorch_lightning as pl
import sys
sys.path.append("data_handling")
sys.path.append("text_analysis")
from classifier import  Model, gen_dataset, split_dataset, yield_batches
from create_dataframe import *   #create_topic_dataframe
from os.path import isfile
import pandas as pd

if __name__ == "__main__":

    if isfile("dumps/topic.pkl"):
        topic = pd.read_pickle("dumps/topic.pkl")
    else:
        topic = create_dataframe()      #create_topic_dataframe

    EPOCHS = 10
    LEARNING_RATE = 1e-3
    BATCH_SIZE = 64
    TOPICS = ["politics", "health", "emotion", "financial", "sport", "science"]
    VOCAB_LEN = 10000

    data_y, data_x = gen_dataset(topic, TOPICS, "topic")

    train_x, test_x = split_dataset(data_x)
    train_y, test_y = split_dataset(data_y)

    train_x = train_x.reshape(len(train_x) // BATCH_SIZE, BATCH_SIZE, len(train_x[0]))
    test_x = test_x.reshape(len(test_x) // BATCH_SIZE, BATCH_SIZE, len(test_x[0]))
    train_y = train_y.reshape(len(train_y) // BATCH_SIZE, BATCH_SIZE, 1)
    test_y = test_y.reshape(len(test_y) // BATCH_SIZE, BATCH_SIZE, 1)
    train_x = from_numpy(train_x).float()
    train_y = from_numpy(train_y).float()
    test_x = from_numpy(test_x).float()
    test_y = from_numpy(test_y).float()

    train = [batch for batch in yield_batches(train_x, train_y)]
    test = [batch for batch in yield_batches(test_x, test_y)]

    train_set = Dataset(train)
    test_set = Dataset(test)

    wandb.login(key="68fded06a6651270206da4fc4c0f175085cadbd7")

    run = wandb.init(
        project="twittos-topic",
        config={
            "learning_rate": LEARNING_RATE,
            "epochs": EPOCHS,
        })
    wandb_logger = WandbLogger()

    trainer = pl.Trainer(
        max_epochs=EPOCHS,
        min_epochs=5,
        devices=1,
        accelerator="gpu",
        logger=wandb_logger
    )


    topic_model = Model(VOCAB_LEN, len(TOPICS), LEARNING_RATE)

    trainer.fit(
        model=topic_model,
        train_dataloaders=DataLoader(dataset=train_set, shuffle=True),
        test_dataloaders=DataLoader(dataset=test_set, shuffle=True)
    )

