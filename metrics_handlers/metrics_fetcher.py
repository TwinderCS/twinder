import numpy as np
import pandas as pd

df_tweets = pd.read_pickle('dumps/tweets.pkl')

def distance(v1 : list, v2 : list):
    """Returns the euclidian distance of v1 and v2"""
    assert(len(v1) == len(v2), "Error distance : vectors with different sizes")
    assert(len(v1) != 0, "Error distance : empty vector")

    return np.sqrt(((v1-v2)**2).sum())

def get_closest_users(username : str, n = 30, N = 'max'):
    """
    Will only consider the first N users 
    Go throught the users and calculate the distances to the user's vector
    and returns the n closest
    """

    df_metric = pd.read_pickle("dumps/metrics.pkl")

    metric = df_metric[df_metric['username'] == username]['metric'].iloc[0]

    
    """The first n users different from the one in argument"""
    users_with_metric = list(df_metric[df_metric['username'] != username][['username', 'metric']].itertuples(index=False, name=None))
    if N == 'max':
        N = len(users_with_metric)

    user_with_dist = np.array([[distance(metric, user_metric), username] for (username, user_metric) in users_with_metric[0:N]])
    

    closest_arg = np.argpartition(user_with_dist, n, axis = 0)[:,0][:n]

    closest_users = user_with_dist[closest_arg, 1]

    return closest_users

def get_random_tweet_user(user : str, df = df_tweets):
    """Gets the first tweet of the user to later display it"""

    tweet = df[df['user'] == user]['text'].iloc[0]
    return tweet