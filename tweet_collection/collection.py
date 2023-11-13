import tweepy
from . import twitter_connection as tc

class TweetCollector:
    def __init__(self):
        """
        Initializes a connection to the API to store collected tweets
        """
        self.api_connection = tc.TwitterConnection()
        self.connection = self.api_connection.api
    def search_collect(self, search, lang="french", count=100):
        return self.connection.search_tweets(search, lang=lang, count=count)
    def user_collect(self, user_id, count=100):
        return self.connection.user_timeline(id=user_id, count=count)
    def __repr__(self):
        print(self.connection)
