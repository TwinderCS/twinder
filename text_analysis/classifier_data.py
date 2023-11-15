import pandas as pd
import numpy as np
import random

DATAFRAME = pd.read_pickle("dumps/emotion.pkl")

#print(df['user'].to_numpy()[0])
TWEETS = DATAFRAME['text'].to_numpy()
OPINIONS = DATAFRAME['polarity'].to_numpy()
TRAIN_FROM_DF = [(TWEETS[i], OPINIONS[i]) for i in range(len(TWEETS))]

np.random.shuffle(TRAIN_FROM_DF)
TRAIN_FROM_DF = TRAIN_FROM_DF[0:10]

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
