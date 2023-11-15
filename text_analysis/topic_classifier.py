import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from classifier_data import DATAFRAME
import pytorch_lightning as pl
from classifier import Model

TOPICS = ["politics", "health", "emotion", "financial", "sport", "science"]

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


topic_model = Model(len(TOPICS))
emotion_model = Model(len(EMOTIONS))

trainer.fit(
    model=...,
    train_dataloaders=DataLoader(dataset=.., shuffle=True)
)


