"""
Multiple utility functions for training the classifier models,
as well as the definition of the torch model
"""
from torch import nn, optim
import torch
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
import wandb
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pytorch_lightning as pl
import pandas as pd

tokenizer = get_tokenizer('spacy')
emotion_vocab = torch.load('dumps/emotion.vocab')
topic_vocab = torch.load('dumps/topic.vocab')

def create_vocabs(tokenizer=tokenizer):
    """
    Generate a vocabulary list with the tokenizer, this is used
    to give the embedding a list of possible vocabulary to classify
    """
    emotion_df = pd.read_pickle("dumps/emotion.pkl")
    topic_df = pd.read_pickle("dumps/topic.pkl")
    topic_df['text'] = topic_df['text'].map(str)
    topic_df.reset_index(inplace=True)
    def yield_tokens(data):
        for text in data['text']:
            yield tokenizer(text)

    emotion_vocab = build_vocab_from_iterator(iterator=yield_tokens(emotion_df), specials=["<unk>", "<pad>"])
    emotion_vocab.set_default_index(emotion_vocab["<unk>"])
    topic_vocab = build_vocab_from_iterator(iterator=yield_tokens(topic_df), specials=["<unk>", "<pad>"])
    topic_vocab.set_default_index(topic_vocab["<unk>"])
    torch.save(emotion_vocab, 'dumps/emotion.vocab')
    torch.save(topic_vocab, 'dumps/topic.vocab')


def gen_dataset(dataframe, classes, classname):
    """
    Takes the dataframes and returns the input and output pairs as lists for the model to train on
    """
    # assign an index to each class
    dataframe['class'] = dataframe[classname].map({classes[idx]: idx for idx in range(len(classes))})
    dataframe['tokens'] = dataframe['text'].map(tokenizer)
    max_len = dataframe['tokens'].map(lambda x: len(x)).max()
    # add padding
    dataframe['tokens'] = dataframe['tokens'].map(lambda tokens: tokens + ["<pad>"] * (max_len - len(tokens)))
    dataframe['token_ids'] = dataframe['tokens'].map(emotion_vocab)

    return dataframe['class'], dataframe['token_ids'].to_numpy()

def split_dataset(dataset, proportion=0.7):
    """
    Used to separate the dataset between the training and testing parts, giving a proportion we want to have of train and test
    """
    train_amount = int(len(dataset) * proportion) # approx percent% des donnees
    return dataset[:train_amount], dataset[train_amount:]

def yield_batches(x, y):
    for i in range(len(x)):
        yield (x[i], y[i])
   
class NLPModel(nn.Module):
    """
    This NLP model works in the following way:
    1. It takes a tokenized string of fixed-length (i.e. always same number of tokens)
    2. Passes it through an embedding matrix which associates a vector of size embedding_dim to each token of the string
    3. It takes the average of these vectors to have one representing the entire sentence (making sure to ignore padding)
    4. It passes through 3 dense layers to return a probability vector (un-normalized) representing the likelihood of the string
    belonging to a given class.
    """
    def __init__(self, vocab, embedding_dim, hidden_dim, output_dim):
        super().__init__()
        self.vocab = vocab
        self.embedding = nn.Embedding(len(vocab), embedding_dim)
        self.dense = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        embedded = self.embedding(x)
        mask = (x != self.vocab["<pad>"])
        mask = mask.unsqueeze(-1)
        embedded = embedded * mask.float()
        embedded = embedded.mean(dim=0)
        return self.dense(embedded)

class Model(pl.LightningModule):
    """
    Pytorch Lightning Module, this enables integrating the training and testing code into the model,
    allowing to train and test more easily on any given dataset
    this also allows loading up the model from a checkpoint, to allow stroing the now-trained model.
    """
    def __init__(self, vocab, output_dim):
        super().__init__()
        self.model = NLPModel(vocab, 1000, 256, output_dim)
        self.loss = nn.CrossEntropyLoss()
        self.tests = 0 # used to measure accuracy
        self.correct = 0 # used to measure accuracy

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
        """
        Unused for testing and training but used when wanting to apply the finished model
        """
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

    def configure_optimizers(self, lr=1e-3):
        return optim.Adam(self.parameters(), lr=lr)
