"""A bot that synchronizes between linkedin and this API."""

try:
    from urllib.parse import urlencode
except ImportError:
    # Python 2.7
    from urllib import urlencode

import os
import requests
from requests_oauthlib import OAuth2

VERIFY_CREDENTIALS = 'https://api.twitter.com/1.1/account/verify_credentials.json'
TWEET_ENDPOINT = "https://api.twitter.com/1.1/statuses/update.json?"

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY", "consumer_key")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET", "consumer_sec")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "access_tok")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "access_sec")


class InvalidCredentials(Exception):
    pass


class Boron(object):
    def __init__(self):
        pass

    @property
    def auth(self):
        return OAuth2(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_secret
        )

    def verify_credentials(self):
        self.get(VERIFY_CREDENTIALS, auth=self.auth)

    @property
    def get(self):
        return requests.get

    @property
    def post(self):
        return requests.post


if __name__ == "__main__":
    pass
