import pytest


def test_helium_builds_correctly(HeliumBot):
    assert HeliumBot.target == 'https://api.github.com/users/qwergram/repos'
    assert HeliumBot.repos == []
    assert not HeliumBot.raw_repos
    assert not HeliumBot.ready_for_local


def test_get_repos(HeliumBot):
    HeliumBot.get_repos()
    assert HeliumBot.raw_repos
    assert HeliumBot.repos


def test_simplify_data_without_get(HeliumBot):
    with pytest.raises(EnvironmentError):
        HeliumBot.simplify_data()


def test_simplify_data(HeliumBot):
    HeliumBot.get_repos()
    snapshot_one = HeliumBot.repos[::]
    HeliumBot.simplify_data()
    snapshot_two = HeliumBot.repos[::]
    assert snapshot_one != snapshot_two
    assert HeliumBot.ready_for_local


def test_online_bot(OnlineHeliumBot):
    with pytest.raises(AttributeError):
        OnlineHeliumBot._hit_endpoint("localhost", "something_else")
