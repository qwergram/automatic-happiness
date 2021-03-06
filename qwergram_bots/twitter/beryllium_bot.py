"""A bot that tweets everything I've posted."""

try:
    from urllib.parse import urlencode
except ImportError:
    # Python 2.7
    from urllib import urlencode

import os
import requests
from requests_oauthlib import OAuth1

VERIFY_CREDENTIALS = 'https://api.twitter.com/1.1/account/verify_credentials.json'
TWEET_ENDPOINT = "https://api.twitter.com/1.1/statuses/update.json?"

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY", "consumer_key")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET", "consumer_sec")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "access_tok")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "access_sec")


class InvalidCredentials(Exception):
    pass


class Beryllium(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.max_length = 140

    @property
    def auth(self):
        return OAuth1(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_secret
        )

    def verify_credentials(self):
        response = self.get(VERIFY_CREDENTIALS, auth=self.auth)
        if not response.ok:
            raise InvalidCredentials("Check .secrets.sh and https://apps.twitter.com/app/12398495/keys/ and make sure the values match.")
        return response.json()

    @property
    def get(self):
        return requests.get

    @property
    def post(self):
        return requests.post

    def tweet(self, tweet):
        # if len(tweet) > 140:
        # raise ValueError("Tweet is too long!")
        encoded = urlencode({'status': tweet})
        response = self.post(TWEET_ENDPOINT + encoded, auth=self.auth)
        assert response.ok, response.json()
        return response.json()


if __name__ == "__main__":
    Bot = Beryllium(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    Bot.verify_credentials()
    import pprint
    pprint.pprint(Bot.tweet("This was tweeted using beryllium_bot (https://github.com/qwergram/automatic-happiness/blob/sprint-1/qwergram_bots/twitter/beryllium_bot.py)!"))
