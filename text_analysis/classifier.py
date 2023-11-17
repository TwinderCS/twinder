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


def yield_tokens(data):
    for text in data['text']:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(iterator=yield_tokens(DATAFRAME), specials=["<unk>", "<pad>"])
vocab.set_default_index(vocab["<unk>"])

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
            nn.Linear(hidden_dim, output_dim),
<<<<<<< HEAD
            nn.ReLU(),
=======
            nn.ReLU()
>>>>>>> ml
        )

    def forward(self, x):
        embedded = self.embedding(x)
        mask = (x != vocab["<pad>"])
        embedded = embedded * mask.float()
        embedded = embedded.mean(dim=...)
        return self.dense(embedded)

class Model(pl.LightningModule):
    def __init__(self, vocab_len, output_dim, learning_rate):
        super().__init__()
        self.model = NLPModel(vocab_len, 1000, 256, output_dim)
        self.loss = nn.CrossEntropyLoss()
        self.learning_rate = learning_rate

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

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=self.learning_rate)

if __name__ == "__main__":
    tokenizer = get_tokenizer('basic english')

    vocab = build_vocab_from_iterator(iterator=yield_tokens(DATAFRAME), specials=["<unk>", "<pad>"])
    vocab.set_default_index(vocab["<unk>"])



