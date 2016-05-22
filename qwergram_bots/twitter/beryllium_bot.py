"""A bot that tweets everything I've posted."""

class Beryllium(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

    @property
    def auth(self):
        return OAuth1(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_secret
        )


if __name__ == "__main__":
    import os
    import requests
    from requests_oauthlib import OAuth1

    CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
