import sys
sys.path.append('text_analysis')
sys.path.append('dumps')
sys.path.append('data_handling')
import torch
import pytorch_lightning as pl
from classifier import Model, vocab, tokenizer
from text_analysis import cleaner
import numpy as np

topic= Model.load_from_checkpoint("dumps/topic_model.ckpt", vocab_len = len(vocab), output_dim = len(topics))
topic.eval()
emotion = Model.load_from_checkpoint("dumps/emotion_model.ckpt", vocab_len = len(vocab), output_dim = len(emotions))
emotion.eval()
max_len = 280

def topic_model(tweet, argmax=True, clean=True, int_output=False):
    global topics
    global topic
    global tokenizer
    global cleaner
    global vocab
    global max_len
    if clean:
        tweet = cleaner(tweet)

    tokens = tokenizer(tweet)
    tokens += ["<pad>"] * (max_len - len(tokens))
    tokens = [vocab[token] for token in tokens]

    tokens = np.array(tokens)
    out = topic(tokens)

    if not argmax:
        return out
    elif int_output:
        return out.argmax()
    else:
        return topics[out.argmax()]
    
def emotion_model(tweet, argmax=True, clean=True, int_output=False):
    global emotions
    global emotion
    global tokenizer
    global cleaner
    global vocab
    global max_len
    if clean:
        tweet = cleaner(tweet)

    tokens = tokenizer(tweet)
    tokens += ["<pad>"] * (max_len - len(tokens))
    tokens = [vocab[token] for token in tokens]

    tokens = np.array(tokens)
    tokens = torch.Tensor(tokens)
    tokens = torch.Tensor(tokens).long()
    out = emotion(tokens)

    if not argmax:
        return out
    elif int_output:
        return out.argmax()
    else:
        return emotions[out.argmax()]

    

    

    
    
