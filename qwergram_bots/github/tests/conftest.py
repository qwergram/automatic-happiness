from github.helium_bot import Helium, GITHUB_ENDPOINT
import pytest

class MockRequests(object):

    pass


class OfflineHelium(Helium):

    def _hit_endpoint(self, target, verb="get"):
        return MockRequests


@pytest.fixture
def HeliumBot():
    return OfflineHelium(GITHUB_ENDPOINT)
