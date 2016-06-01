import pytest


def test_oxygen_builds_correctly(OxygenBot):
    assert OxygenBot.base_endpoint
    assert OxygenBot.issues_target
    assert OxygenBot.language_target
    assert OxygenBot.commits_target
    assert OxygenBot.milestone_target


def test_online_bot(OnlineOxygenBot):
    with pytest.raises(AttributeError):
        OnlineOxygenBot._hit_endpoint("localhost", "something_else")


def test_get_basic_data(OxygenBot):
    response = OxygenBot.get_basic_data()
    assert "size" in response.keys()
    assert "open_issues" in response.keys()
    assert "homepage" in response.keys()
    assert "updated_at" in response.keys()


def test_get_languages(OxygenBot):
    assert OxygenBot.get_languages() == OxygenBot._hit_endpoint('some_endpoint')


def test_get_commits(OxygenBot):
    assert OxygenBot.get_commit_by_sha('some_number') == OxygenBot._hit_endpoint('some_endpoint')


def test_get_milestones(OxygenBot):
    assert OxygenBot.get_milestones() == OxygenBot._hit_endpoint('some_endpoint')
