import pandas as pd

def get_hashtags(text):
    tgs = []
    for word in text.split(" ")
        try:
            if word[0] == "#":
                tgs.append(word)
    return tgs

def get_mentions(text):
    mts = []
    for word in text.split(" ")
        try:
            if word[0] == "@":
                mts.append(word)
    return mts

def polarity(num):
    if num == 0:
        return 'negative'
    elif num == 2:
        return 'neutral'
    elif num == 4:
        return 'positive'

df = pd.read_csv("../dumps/tweets.csv", index_col="ids", usecols=[0,1,2,4,5])
df['date'] = pd.to_datetime(df['date'], format="%a %b %d %H:%M:%S PDT %Y")
df['hashtags'] = df['text'].map(get_hashtags)
df['mentions'] = df['text'].map(get_mentions)
df['polarity'] = df['polarity'].map(polarity) # transformer 0, 2, 4 en negative, neutral, positive


df.to_pickle("../dumps/df.pkl")
