"""Get a list of the most recent stuff I've been doing on github"""
import requests

GITHUB_ENDPOINT = "https://api.github.com"
RAW_ENDPOINT = "https://raw.githubusercontent.com/{owner_repo_name}/master/README.md"


class Helium(object):

    def __init__(self, github_endpoint):
        self.target = github_endpoint + '/users/qwergram/repos'
        self.repos = []

        self.raw_repos = False
        self.ready_for_local = False

    def _hit_endpoint(self, target, verb="get"):
        return getattr(requests, verb)(target).json()

    def get_repos(self):
        self.raw_repos = True
        self.repos = self._hit_endpoint(self.target)

    def simplify_data(self):
        if self.raw_repos:
            for i, repo in enumerate(self.repos):
                display_content = {
                    "id": None,
                    "clone_url": None,
                    "commits_url": None,
                    "created_at": None,
                    "description": None,
                    "full_name": None,
                    "homepage": None,
                    "html_url": None,
                    "open_issues": None,
                    "pushed_at": None,
                    "size": None,
                    "updated_at": None,
                    "watchers": None,
                    "language": None,
                }
                for key in display_content:
                    display_content[key] = repo[key]
                display_content['readme'] = RAW_ENDPOINT.format(owner_repo_name=display_content['full_name'])
                self.repos[i] = display_content
            self.ready_for_local = True
        else:
            raise EnvironmentError("Get repos first (Helium.get_repos)")


if __name__ == "__main__":
    Bot = Helium(GITHUB_ENDPOINT)
    Bot.get_repos()
    Bot.simplify_data()
