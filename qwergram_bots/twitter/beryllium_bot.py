"""A bot that tweets everything I've posted."""

from urllib.parse import urlencode

VERIFY_CREDENTIALS = 'https://api.twitter.com/1.1/account/verify_credentials.json'
TWEET_ENDPOINT = "https://api.twitter.com/1.1/statuses/update.json?"


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
        response = requests.get(VERIFY_CREDENTIALS, auth=self.auth)
        if not response.ok:
            raise InvalidCredentials("Check .secrets.sh and https://apps.twitter.com/app/12398495/keys/ and make sure the values match.")
        return response.json()

    @property
    def post(self):
        return requests.post

    def tweet(self, tweet):
        if len(tweet) > 140:
            raise ValueError("Tweet is too long!")
        encoded = urlencode({'status': tweet})
        response = self.post(TWEET_ENDPOINT + encoded, auth=auth)
        assert response.ok, response.json()


if __name__ == "__main__":
    import os
    import requests
    from requests_oauthlib import OAuth1

    CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    Bot = Beryllium(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    import pprint
    pprint.pprint(Bot.verify_credentials())
