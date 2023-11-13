import pandas as pd

df = pd.read_csv("../dumps/tweets.csv", index_col="ids", usecols=[0,1,2,4,5])
df['date'] = pd.to_datetime(df['date'], format="%a %b %d %H:%M:%S PDT %Y")
df.to_pickle("../dumps/df.pkl")
