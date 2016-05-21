from github.helium_bot import Helium, GITHUB_ENDPOINT
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


@pytest.fixture
def HeliumBot():
    return OfflineHelium(GITHUB_ENDPOINT)


@pytest.fixture
def OnlineHeliumBot():
    return Helium(GITHUB_ENDPOINT)
