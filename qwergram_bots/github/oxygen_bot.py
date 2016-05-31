"""OxygenBot is in charge of checking on the health of this repo."""
from github.helium_bot import GITHUB_ENDPOINT, Helium
import requests
import json

BASE_ENDPOINT = "{}/repos/qwergram/automatic-happiness".format(GITHUB_ENDPOINT)


class Oxygen(object):

    def __init__(self, base_endpoint):
        self.issues_target = "{}/issues/events".format(base_endpoint)
        self.language_target = "{}/languages".format(base_endpoint)

    def _hit_endpoint(self, target, verb="get"):
        return getattr(requests, verb)(target).json()

    def get_languages(self):
        response = self._hit_endpoint(self.language_target)
        return response

    def get_latest_commits(self, amount=10):
        pass


if __name__ == "__main__":
    OBot = Oxygen(BASE_ENDPOINT)
    print(OBot.get_languages())
