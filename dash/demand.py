import pandas as pd
def import_tweets_from_username(username: str) -> pd.DataFrame:
    df = pd.read_pickle(dumps/df.pkl)
    tweets = df.copy()
    tweets = tweets[tweets['user'] == username]
    return tweets