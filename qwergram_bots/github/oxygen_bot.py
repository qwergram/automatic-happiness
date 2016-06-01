"""OxygenBot is in charge of checking on the health of this repo."""
from github.helium_bot import GITHUB_ENDPOINT
from github.flourine_bot import Flourine, LOCAL_ENDPOINT
import requests
import os

BASE_ENDPOINT = "{}/repos/qwergram/automatic-happiness".format(GITHUB_ENDPOINT)


class Oxygen(object):

    def __init__(self, base_endpoint):
        self.base_endpoint = base_endpoint
        self.issues_target = "{}/issues/events".format(self.base_endpoint)
        self.language_target = "{}/languages".format(self.base_endpoint)
        self.commits_target = "{}/commits".format(self.base_endpoint)
        self.milestone_target = "{}/milestones".format(self.base_endpoint)

    def _hit_endpoint(self, target, verb="get"):
        return getattr(requests, verb)(target).json()

    def get_basic_data(self):
        response = self._hit_endpoint(self.base_endpoint)
        return {
            "size": response['size'],
            "open_issues": response['open_issues'],
            "homepage": response['homepage'],
            "updated_at": response['updated_at']
        }

    def get_languages(self):
        response = self._hit_endpoint(self.language_target)
        return response

    def get_commit_by_sha(self, sha):
        return self._hit_endpoint(self.commits_target + '/{}'.format(sha))

    def get_latest_commits(self, amount=10):

        response = self._hit_endpoint(self.commits_target)[:amount]

        for i, commit in enumerate(response):
            response[i] = {}
            details = self.get_commit_by_sha(commit['sha'])
            response[i]['sha'] = commit['sha']
            response[i]['author'] = commit['commit']['author']
            response[i]['message'] = commit['commit']['message']
            response[i]['stats'] = details['stats']
            # response[i]['files'] = details['files']

        return response

    def get_milestones(self):
        return self._hit_endpoint(self.milestone_target)


if __name__ == "__main__":
    admin = os.environ['ADMIN_USER']
    admin_pass = os.environ['ADMIN_PASS']
    OBot = Oxygen(BASE_ENDPOINT)
    FBot = Flourine(LOCAL_ENDPOINT, admin, admin_pass)
    FBot.upload_data("languages", OBot.get_languages())
    FBot.upload_data("latest_commits", OBot.get_latest_commits())
    FBot.upload_data("milestones", OBot.get_milestones())
