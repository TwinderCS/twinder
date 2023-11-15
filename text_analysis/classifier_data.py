import pandas as pd
import numpy as np
import random

DATAFRAME = pd.read_pickle("dumps/df.pkl")

#print(df['user'].to_numpy()[0])
TWEETS = df['text'].to_numpy()
OPINIONS = df['polarity'].to_numpy()
TRAIN_FROM_DF = [(tweets[i], opinions[i]) for i in range(len(tweets))]

np.random.shuffle(train_from_df)
<<<<<<< HEAD
TRAIN_FROM_DF = TRAIN_FROM_DF[0:10000]

TRAIN = [('I love this sandwich.', 'positive'),
    ('this is an amazing place!', 'positive'),
    ('I feel very good about these beers.', 'positive'),
    ('this is my best work.', 'positive'),
    ("what an awesome view", 'positive'),
    ('I do not like this restaurant', 'negative'),
    ('I am tired of this stuff.', 'negative'),
    ("I can't deal with this", 'negative'),
    ('he is my sworn enemy!', 'negative'),
    ('my boss is horrible.', 'negative'),
    ('the beer was good.', 'positive'),
    ('I do not enjoy my job', 'negative'),
    ("I ain't feeling dandy today.", 'negative'),
    ("I feel amazing!", 'positive'),
    ('Gary is a friend of mine.', 'positive'),
    ("I can't believe I'm doing this.", 'negative')]
=======
train_from_df = train_from_df[0:10000]

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
>>>>>>> e49cb2ef589d67f43d7b36203059c244eb08e8b7
