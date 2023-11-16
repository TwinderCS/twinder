"""Pour lire les db et numpy"""
import pandas as pd
import numpy as np

DATAFRAME = pd.read_pickle("dumps/df.pkl")


TWEETS = DATAFRAME['text'].to_numpy()
EMOTIONS = DATAFRAME['polarity'].to_numpy()
TRAIN_FROM_DF_ALL = [(TWEETS[i], EMOTIONS[i]) for i in range(len(TWEETS))]

np.random.shuffle(TRAIN_FROM_DF_ALL)


TRAIN_FROM_DF = TRAIN_FROM_DF_ALL[0:2000] #Otherwise it takes wayyy to long
print(TRAIN_FROM_DF[0])
train = [('I love this sandwich.', 'pos'),
    ('this is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('he is my sworn enemy!', 'neg'),
    ('my boss is horrible.', 'neg'),
    ('the beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')]
