import torch
import pytorch_lightning as pl
import numpy as np
import sys
sys.path.append("metrics_handlers")
sys.path.append("text_analysis")
from classifier import Model, vocab, tokenizer
from metrics import emotions, topics, max_len
from text_analysis import cleaner

topic = Model.load_from_checkpoint("dumps/topic_model.ckpt")
emotion = Model.load_from_checkpoint("dumps/emotion_model.ckpt")

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
    tokens = torch.Tensor(tokens)
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
    out = emotion(tokens)

    if not argmax:
        return out
    elif int_output:
        return out.argmax()
    else:
        return emotions[out.argmax()]

    

    

    
    
