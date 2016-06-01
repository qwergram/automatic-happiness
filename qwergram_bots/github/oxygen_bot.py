"""OxygenBot is in charge of checking on the health of this repo."""
from github.helium_bot import GITHUB_ENDPOINT, Helium
import requests
import json

BASE_ENDPOINT = "{}/repos/qwergram/automatic-happiness".format(GITHUB_ENDPOINT)


class Oxygen(object):

    def __init__(self, base_endpoint):
        self.issues_target = "{}/issues/events".format(base_endpoint)
        self.language_target = "{}/languages".format(base_endpoint)
        self.commits_target = "{}/commits".format(base_endpoint)
        self.milestone_target = "{}/milestones".format(base_endpoint)

    def _hit_endpoint(self, target, verb="get"):
        return getattr(requests, verb)(target).json()

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
    OBot = Oxygen(BASE_ENDPOINT)
    # print(OBot.get_languages())
    # print(OBot.get_latest_commits())
    print(OBot.get_milestones())
