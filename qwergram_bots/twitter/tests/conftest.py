import pytest
from twitter.beryllium_bot import Beryllium, InvalidCredentials


class MockRequests(object):

    def __init__(self):
        self.post_called = 0
        self.get_called = 0

    class MockResponse(object):

        def json(self):
            return {"some": "json", "json": True}

    def get(self, *args, **kwargs):
        self.get_called += 1
        return MockRequests.MockResponse()

    def post(self, *args, **kwargs):
        self.post_called += 1
        return MockRequests.MockResponse()


class OfflineBeryllium(Beryllium):

    def __init__(self, *args, **kwargs):
        self.__TEST_ONLY_mock_requests = MockRequests()

    @property
    def get(self, *args, **kwargs):
        return self.__TEST_ONLY_mock_requests.get

    @property
    def post(self, *args, **kwargs):
        return self.__TEST_ONLY_mock_requests.post


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
