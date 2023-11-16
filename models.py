import torch
import pytorch_lighting as pl
from text_analysis.classifier import Model, vocab, tokenizer
from metrics import emotions, topics
from text_analysis.text_analysis import get_lemmas_from_tweet as lemmatizer
from text_analysis.classifier_data import max_len

topic = Model.load_from_checkpoint("dumps/topic_model.ckpt")
emotion = Model.load_from_checkpoint("dumps/emotion_model.ckpt")

def topic_model(tweet, argmax=True, lemmatize=True, vocab=vocab, int_output=False):
    global topics
    global topic
    global tokenizer
    global lemmatizer
    global vocab
    global max_len
    if lemmatize:
        tweet = lemmatizer(tweet)

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
    
def emotion_model(tweet, argmax=True, lemmatize=True, lemmatizer=get_lemmas_from_tweet, vocab=vocab, int_output=False):
    global emotions
    global emotion
    global tokenizer
    global lemmatizer
    global vocab
    global max_len
    if lemmatize:
        tweet = lemmatizer(tweet)

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

    

    

    
    
