import torch
from torch import nn, optim
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pytorch_lightning as pl
import spacy
import pandas as pd

## TOKENIZATION
df = pd.read_pickle("dumps/emotion.pkl")
tokenizer = get_tokenizer('spacy')
def yield_tokens(data):
    for text in data['text']:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(iterator=yield_tokens(df), specials=["<unk>", "<pad>"])
vocab.set_default_index(vocab["<unk>"])

EPOCHS = 10
LEARNING_RATE = 1e-3
BATCH_SIZE = 64

def gen_dataset(dataframe, classes, classname):
    # assign an index to each class
    dataframe['class'] = dataframe[classname].map({classes[idx]: idx for idx in range(len(classes))})
    dataframe['tokens'] = dataframe['text'].map(tokenizer)
    max_len = dataframe['tokens'].map(lambda x: len(x)).max()
    # add padding
    dataframe['tokens'] = dataframe['tokens'].map(lambda tokens: tokens + ["<pad>"] * (max_len - len(tokens)))
    dataframe['token_ids'] = dataframe['tokens'].map(vocab)

    return dataframe['class'], dataframe['token_ids'].to_numpy()

def split_dataset(dataset, percent=0.7):
    train_amount = int(len(dataset) * percent) # approx percent% des donnees
    return dataset[:train_amount], dataset[train_amount:]

def yield_batches(x, y):
    for i in range(len(x)):
        yield (x[i], y[i])
   
class NLPModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.dense = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        mask = (x != vocab["<pad>"])
        mask = mask.unsqueeze(-1)
        embedded = embedded * mask.float()
        embedded = embedded.mean(dim=0)
        return self.dense(embedded)

class Model(pl.LightningModule):
    def __init__(self, vocab_len, output_dim):
        super().__init__()
        self.model = NLPModel(vocab_len, 1000, 256, output_dim)
        self.loss = nn.CrossEntropyLoss()
        self.tests = 0
        self.correct = 0

    def training_step(self, batch):
        x, y = batch
        y_hat = self.model(x)
        y = y.squeeze(0)
        y = y.squeeze(-1)
        y_hat = y_hat.squeeze(0)
        loss = self.loss(y_hat, y)
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.model(x)
        loss = self.loss(y_hat, y)
        self.log("val_loss", loss, prog_bar=True)

    def forward(self, x):
        return self.model(x)

    def test_step(self, batch):
        x, y = batch
        y_hat = self.model(x)
        y = y.squeeze(0)
        y = y.squeeze(-1)
        y_hat = y_hat.squeeze(0)
        self.tests += BATCH_SIZE
        loss = self.loss(y_hat, y)
        self.log("test_loss", loss, prog_bar=True)
        self.correct += (y_hat.argmax(dim=-1) == y).float().sum()
        self.log("accuracy", self.correct/self.tests, prog_bar=True)

    def configure_optimizers(self, lr=LEARNING_RATE):
        return optim.Adam(self.parameters(), lr=lr)
