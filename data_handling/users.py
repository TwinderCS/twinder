import pandas as pd
from metrics import topics, emotions

tweets = pd.read_pickle("dumps/tweets.pkl")

users = pd.DataFrame()
users['user'] = tweets['user'].unique()

users['tweets'] = users['user'].map(lambda user: [tweet_id for tweet_id in tweets['id'].where(
                                        tweets['user'] == user, -1
                                    )
                                    if tweet_id != -1])
def compute_class(user_tweets, class_type, class_name):
    global tweets
    total = len(user_tweets)
    class_matches = 0
    for tweet in user_tweets:
        if tweets[class_type][tweet] == class_name:
            class_matches += 1
    return class_matches/total

for topic in topics:
    users[topic] = users['tweets'].map(
        lambda tweet_list: compute_class(tweet_list, 'topic', topic)
    )
for emotion in emotions:
    users[emotion] = users['tweets'].map(
        lambda tweet_list: compute_class(tweet_list, 'emotion', emotion)
    )

users['vec'] = users[topics + emotions].map(
    lambda values: np.array([val for val in values])
)
