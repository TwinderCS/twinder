import sys
sys.path.append('classifiers')
sys.path.append('dumps')
sys.path.append('data_handling')
import torch
import pytorch_lightning as pl
import numpy as np
sys.path.append("metrics_handlers")
from nlp_models import Model, topic_vocab, tokenizer, emotion_vocab
from cleaner import cleaner
import numpy as np

max_len = 280
emotions = ["joy", "sadness", "fear", "anger", "surprise", "neutral", "shame", "disgust"]
topics = ["politics", "health", "emotion", "financial", "sport", "science"]

topic = Model.load_from_checkpoint("dumps/topic_model.ckpt", vocab = topic_vocab, output_dim = len(topics))
topic.eval()
emotion = Model.load_from_checkpoint("dumps/emotion_model.ckpt", vocab = emotion_vocab, output_dim = len(emotions))
emotion.eval()


def topic_model(tweet : str, argmax = True, clean = True, int_output = False):
    """
    Evaluates the string input through the topic torch NLP model and returns either:
    - a non-normalized (i.e not in the range [0,1]) probability vector for each topic (argmax=False)
    - a string output of the topic (argmax=True, int_output=False)
    - an integer output of the topic (int_output=False)
    """
    global topics
    global topic
    global tokenizer
    global cleaner
    global topic_vocab
    global max_len
    if clean:
        tweet = cleaner(tweet)

    tokens = tokenizer(tweet)
    tokens += ["<pad>"] * (max_len - len(tokens))
    tokens = [topic_vocab[token] for token in tokens]

    tokens = np.array(tokens)
    tokens = torch.Tensor(tokens).long()
    out = topic(tokens)

    if not argmax:
        return out
    elif int_output:
        return out.argmax()
    else:
        return topics[out.argmax()]
    
def emotion_model(tweet : str, argmax=True, clean=True, int_output=False):
    """
    Evaluates the string input through the emotion torch NLP model and returns either:
    - a non-normalized (i.e not in the range [0,1]) probability vector for each emotion (argmax=False)
    - a string output of the emotion (argmax=True, int_output=False)
    - an integer output of the emotion (int_output=False)
    """
    global emotions
    global emotion
    global tokenizer
    global cleaner
    global emotion_vocab
    global max_len
    if clean:
        tweet = cleaner(tweet)

    tokens = tokenizer(tweet)
    tokens += ["<pad>"] * (max_len - len(tokens))
    tokens = [emotion_vocab[token] for token in tokens]

    tokens = np.array(tokens)
    tokens = torch.Tensor(tokens).long()
    out = emotion(tokens)

    if not argmax:
        return out
    elif int_output:
        return out.argmax()
    else:
        return emotions[out.argmax()]

    

    

    
    
