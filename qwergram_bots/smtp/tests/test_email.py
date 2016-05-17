"""Test Hydrogen bot functionality"""

def test_hydrogen_initialization(HydrogenBot):
    assert HydrogenBot.emails == []
    assert HydrogenBot.in_inbox is False
    assert HydrogenBot.opened_inbox is False
    assert HydrogenBot.authenticated is False
    assert HydrogenBot.connected is False
