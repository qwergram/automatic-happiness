import pytest
from twitter.beryllium_bot import Beryllium


class MockRequests(object):

    class MockResponse(object):

        ok = True

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
    return OfflineBeryllium("consumer_key", "consumer_secret", "access_token", "access_secret")


@pytest.fixture
def BadBerylliumBot():
    bot = OfflineBeryllium("consumer_key", "consumer_secret", "access_token", "access_secret")
    bot.MockResponse.ok = False
