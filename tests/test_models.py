import pytest
import torch
import numpy as np
from models import topic_model, emotion_model

@pytest.fixture
def sample_tweet():
    return "This is a sample tweet."

def test_topic_model(sample_tweet):
    result = topic_model(sample_tweet, argmax=True, clean=True, int_output=False)
    # Add specific assertions based on your expected behavior

def test_emotion_model(sample_tweet):
    result = emotion_model(sample_tweet, argmax=True, clean=True, int_output=False)
    # Add specific assertions based on your expected behavior

# Add more test cases as needed
