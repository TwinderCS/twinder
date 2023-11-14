import pandas as pd
import numpy as np
import random

df = pd.read_pickle("dumps/df.pkl")

#print(df['user'].to_numpy()[0])
tweets = df['text'].to_numpy()
opinions = df['polarity'].to_numpy()
train_from_df = [(tweets[i], opinions[i]) for i in range(len(tweets))]
np.random.shuffle(train_from_df)
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
