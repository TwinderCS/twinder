import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from classifier_data import DATAFRAME
import pytorch_lightning as pl
from classifier import Model


EPOCHS = 10
LEARNING_RATE = 1e-3
BATCH_SIZE = 64
EMOTIONS = ["joy", "sadness", "fear", "anger", "surprise"]
wandb.login(key="68fded06a6651270206da4fc4c0f175085cadbd7")

run = wandb.init(
    project="twittos-emotion",
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


emotion_model = Model(len(EMOTIONS))

trainer.fit(
    model=emotion_model,
    train_dataloaders=DataLoader(dataset=.., shuffle=True)
)


