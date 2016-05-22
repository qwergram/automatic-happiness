import pytest
from twitter.beryllium_bot import Beryllium, InvalidCredentials


class MockRequests(object):

    class MockResponse(object):

        def json(self):
            return {"some": "json", "json": True}

    def get(self, *args, **kwargs):
        return MockRequests.MockResponse()

    def post(self, *args, **kwargs):
        return MockRequests.MockResponse()


class OfflineBeryllium(Beryllium):

    @property
    def get(self, *args, **kwargs):
        return MockRequests().get

    @property
    def post(self, *args, **kwargs):
        return MockRequests().post


@pytest.fixture
def BerylliumBot():
    MockRequests.MockResponse.ok = True
    return OfflineBeryllium("consumer_key", "consumer_secret", "access_token", "access_secret")


@pytest.fixture
def BadBerylliumBot():
    bot = OfflineBeryllium("consumer_key", "consumer_secret", "access_token", "access_secret")
    MockRequests.MockResponse.ok = False
    return bot


@pytest.fixture
def BadCredentials():
    return InvalidCredentials


@pytest.fixture
def OnlineBerylliumBot():
    return Beryllium("consumer_key", "consumer_secret", "access_token", "access_secret")
