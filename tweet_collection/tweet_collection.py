import tweepy
import json

class TweetCollection:
    def __init__(self, twitter_connection):
        """
        Will later be used for collections
        """
    
    def store_tweets(self, tweets, filename):
        with open(filename, "w") as out_file:
            json.dump(tweets, out_file)