"""Test Hydrogen bot functionality"""
import pytest


def test_hydrogen_initialization(HydrogenBot):
    assert HydrogenBot.emails == []
    assert HydrogenBot.in_inbox is False
    assert HydrogenBot.opened_inbox is False
    assert HydrogenBot.authenticated is False
    assert HydrogenBot.connected is False


def test_connect_executes(HydrogenBot):
    HydrogenBot.connect()
    assert HydrogenBot.connected
    assert HydrogenBot.mail
    assert HydrogenBot.email_imap


def test_authenticate_without_connect(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.authenticate()


def test_authenticate_executes(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    assert HydrogenBot.connected
    assert HydrogenBot.authenticated
    assert HydrogenBot.mail.login_count == 1


def test_checkout_inbox_without_connect(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.checkout_inbox()


def test_checkout_inbox_without_authenticate(HydrogenBot):
    HydrogenBot.connect()
    with pytest.raises(EnvironmentError):
        HydrogenBot.checkout_inbox()


def test_checkout_inbox_executes(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    assert HydrogenBot.in_inbox
    assert HydrogenBot.mail.select_count == 1


def test_get_emails_without_connect(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.get_emails()


def test_get_emails_without_authenticate(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.get_emails()
