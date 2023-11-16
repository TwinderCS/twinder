import torch
from torch import nn, optim
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from data_handling import DATAFRAME
import pytorch_lightning as pl


## TOKENIZATION

tokenizer = get_tokenizer('basic english')

def yield_tokens(data):
    for text in data['text']:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(iterator=yield_tokens(DATAFRAME), specials=["<unk>", "<pad>"])
vocab.set_default_index(vocab["<unk>"])

EPOCHS = 10
LEARNING_RATE = 1e-3
BATCH_SIZE = 64
VOCAB_LEN = len(vocab)
VOCAB = vocab

class NLPModel(nn.Module):
    def __init__(self):
        super().__init__(vocab_size, embedding_dim, hidden_dim, output_dim):
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.hidden1 = nn.Linear(embedding_dim, hidden_dim)
        self.hidden2 = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        embedded = self.embedding(x)
        mask = (x != vocab["<pad>"])
        embedded = embedded * mask.float()
        embedded = embedded.mean(dim=...)
        out = self.hidden1(embedded)
        out = self.relu(out)
        out = self.hidden2(out)
        out = self.relu(out)
        return out

class Model(pl.LightningModule):
    def __init__(self, output_dim):
        super().__init__()
        self.model = NLPModel(VOCAB_LEN, 1000, 256, output_dim)
        self.loss = nn.CrossEntropyLoss()

    def training_step(self, batch):
        x, y = batch
        y_hat = self.model(x)
        loss = self.loss(y, y_hat)
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.model(x)
        loss = self.loss(y_hat, y)
        self.log("val_loss", loss, prog_bar=True)

    def test_step(self, batch):
        x, y = batch
        y_hat = self.model(x)
        loss = self.loss(y_hat, y)
        self.log("test_loss", loss, prog_bar=True)

    def configure_optimizers(self, lr=LEARNING_RATE):
        return optim.Adam(self.parameters(), lr=lr)



