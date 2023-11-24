import torch
from torch.utils.data import DataLoader
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
import pytest
import pandas as pd
import sys
sys.path.append("classifiers")
from nlp_models import gen_dataset, split_dataset, yield_batches, NLPModel, Model

# Assuming 'dumps/df.pkl' contains a pickled DataFrame with 'text' and 'class' columns

@pytest.fixture
def sample_data():
    tokenizer = get_tokenizer('spacy')
    df = pd.read_pickle("dumps/df.pkl")
    classes = ['class1', 'class2', 'class3']  # Replace with your actual class names
    class_name = 'class'
    
    yield gen_dataset(df, classes, class_name)

def test_gen_dataset(sample_data):
    train_data, test_data = split_dataset(sample_data)
    assert len(train_data) > 0
    assert len(test_data) > 0

def test_yield_batches(sample_data):
    train_data, _ = split_dataset(sample_data)
    x, y = sample_data
    batch_gen = yield_batches(x, y)
    for i, (batch_x, batch_y) in enumerate(batch_gen):
        assert torch.is_tensor(batch_x)
        assert torch.is_tensor(batch_y)

def test_NLPModel():
    vocab_size = 10000  # Replace with your actual vocab size
    embedding_dim = 100
    hidden_dim = 256
    output_dim = 3  # Replace with your actual number of classes
    model = NLPModel(vocab_size, embedding_dim, hidden_dim, output_dim)
    x = torch.randint(0, vocab_size, (BATCH_SIZE, 10))  # Example input tensor
    output = model(x)
    assert output.shape == (BATCH_SIZE, output_dim)

def test_Model():
    vocab_size = 10000  # Replace with your actual vocab size
    output_dim = 3  # Replace with your actual number of classes
    model = Model(vocab_size, output_dim)
    x = torch.randint(0, vocab_size, (BATCH_SIZE, 10))  # Example input tensor
    output = model(x)
    assert isinstance(output, torch.Tensor)

# Add more tests as needed
