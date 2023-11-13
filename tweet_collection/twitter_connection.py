from credentials import *
import tweepy

class TwitterConnection:
    """
    Object used to access the twitter API
    """
    def __init__(self):
        """
        Utility function to setup the Twitter's API
        with an access keys provided in a file credentials.py
        :return: the authentified API
        """
        # Authentication and access using keys:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication:
        self.api = tweepy.API(auth)
        


