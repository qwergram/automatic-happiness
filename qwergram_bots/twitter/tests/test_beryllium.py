"""Test BerylliumBot and see if it's twitter functionalities work."""
import pytest


def test_berrylium_init(BerylliumBot):
    assert BerylliumBot.consumer_key
    assert BerylliumBot.consumer_secret
    assert BerylliumBot.access_token
    assert BerylliumBot.access_secret
    assert BerylliumBot.access_secret
    assert BerylliumBot.max_length


def test_berrylium_auth(BerylliumBot):
    from requests_oauthlib import OAuth1
    assert isinstance(BerylliumBot.auth, OAuth1)


def test_berrylium_verify_credentials(BerylliumBot):
    response = BerylliumBot.verify_credentials()
    assert response == {"some": "json", "json": True}


def test_berrylium_verify_credentials_fail(BadBerylliumBot, BadCredentials):
    with pytest.raises(BadCredentials):
        BadBerylliumBot.verify_credentials()
