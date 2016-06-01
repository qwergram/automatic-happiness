import pytest


def test_flourine_inits(FlourineBot):
    assert FlourineBot.local_endpoint
    assert FlourineBot.admin
    assert FlourineBot.admin_pass


def test_get_url_from_name(FlourineBot):
    assert FlourineBot.get_url_from_name("random_name") == "http://a-url.com"


def test_upload_data(FlourineBot):
    assert FlourineBot.upload_data("name", {"value": "bar"}) == FlourineBot._hit_endpoint()


def test_upload_data_already_exists(BadFlourineBot):
    assert BadFlourineBot.upload_data("name", {"value": "bar"}) == BadFlourineBot._hit_endpoint()
