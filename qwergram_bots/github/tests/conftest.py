from github.helium_bot import Helium, GITHUB_ENDPOINT
from github.oxygen_bot import Oxygen, BASE_ENDPOINT
import pytest


class OfflineHelium(Helium):

    def _hit_endpoint(self, target, verb="get"):
        return [{
            "open_issues": 28,
            "id": 58597301,
            "html_url": "https://github.com/qwergram/automatic-happiness",
            "clone_url": "https://github.com/qwergram/automatic-happiness.git",
            "size": 928,
            "full_name": "qwergram/automatic-happiness",
            "homepage": "http://qwergram.github.io",
            "pushed_at": "2016-05-20T22:13:08Z",
            "updated_at": "2016-05-15T06:38:49Z",
            "description": "Making the Martians jealous since 1942",
            "watchers": 0,
            "created_at": "2016-05-12T01:39:52Z",
            "commits_url": "https://api.github.com/repos/qwergram/automatic-happiness/commits{/sha}",
            "language": "Definitely not Assembly",
            "extra_garbage": "Cats have 3 hearts",
            "fictional fact": "Waffles were sacraficed to the Queen in 1435",
        }]


class OfflineOxygen(Oxygen):

    def _hit_endpoint(self, target, verb="get"):
        return {
            "size": 1032,
            "open_issues": 12,
            "homepage": "qwergram.github.io",
            "updated_at": "yesterday",

            "sha": "some number",
            "commit": {
                "author": "Norton Pengra",
                "message": "This is a commit message (#420)",
            },
            "stats": ["stats"],
        }


class OfflineOxygenList(Oxygen):

    def _hit_endpoint(self, target, verb="get"):
        return [{
            "size": 1032,
            "open_issues": 12,
            "homepage": "qwergram.github.io",
            "updated_at": "yesterday",

            "sha": "some number",
            "commit": {
                "author": "Norton Pengra",
                "message": "This is a commit message (#420)",
            },
            "stats": ["stats"],
        }]

    def get_commit_by_sha(self, sha):
        return {'stats': 'something'}


@pytest.fixture
def HeliumBot():
    return OfflineHelium(GITHUB_ENDPOINT)


@pytest.fixture
def OnlineHeliumBot():
    return Helium(GITHUB_ENDPOINT)


@pytest.fixture
def OxygenBot():
    return OfflineOxygen(BASE_ENDPOINT)


@pytest.fixture
def OnlineOxygenBot():
    return Oxygen(BASE_ENDPOINT)


@pytest.fixture
def OxygenBotLatestCommitsTest():
    return OfflineOxygenList(BASE_ENDPOINT)
