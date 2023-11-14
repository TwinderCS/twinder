import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

df = pd.read_pickle("dumps/df.pkl")

print(df['text'].iloc[70])

#tfav = pd.Series(data=df['polarity'].values, index=df['date'])


# Likes vs retweets visualization:
#tfav.plot(figsize=(16,4), label="Polarity", legend=True)

#plt.show()


