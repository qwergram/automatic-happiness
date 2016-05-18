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
    HydrogenBot.connect()
    with pytest.raises(EnvironmentError):
        HydrogenBot.get_emails()


def test_get_emails_without_checkout(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    with pytest.raises(EnvironmentError):
        HydrogenBot.get_emails()


def test_get_emails_executes(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    HydrogenBot.get_emails()
    assert HydrogenBot.mail.search_count == 1
    assert HydrogenBot.emails == [b'0', b'1']
    assert HydrogenBot.opened_inbox is True


def test_read_emails_without_connect(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.read_emails()


def test_read_emails_without_authenticate(HydrogenBot):
    HydrogenBot.connect()
    with pytest.raises(EnvironmentError):
        HydrogenBot.read_emails()


def test_read_emails_without_checkout(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    with pytest.raises(EnvironmentError):
        HydrogenBot.read_emails()


def test_read_emails_without_get_emails(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    with pytest.raises(EnvironmentError):
        HydrogenBot.read_emails()


def test_read_emails_executes(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    HydrogenBot.get_emails()
    first_snap = [str(email) for email in HydrogenBot.emails]
    HydrogenBot.read_emails()
    second_snap = [str(email) for email in HydrogenBot.emails]
    assert first_snap != second_snap
    assert HydrogenBot.raw_emails
    assert HydrogenBot.mail.fetch_count == 2


def test_parse_emails_without_connect(HydrogenBot):
    with pytest.raises(EnvironmentError):
        HydrogenBot.parse_emails()


def test_parse_emails_without_authenticate(HydrogenBot):
    HydrogenBot.connect()
    with pytest.raises(EnvironmentError):
        HydrogenBot.parse_emails()


def test_parse_emails_without_checkout(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    with pytest.raises(EnvironmentError):
        HydrogenBot.parse_emails()


def test_parse_emails_without_get_emails(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    with pytest.raises(EnvironmentError):
        HydrogenBot.parse_emails()


def test_parse_emails_without_read_emails(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    HydrogenBot.get_emails()
    with pytest.raises(EnvironmentError):
        HydrogenBot.parse_emails()


def test_parse_emails_executes(HydrogenBot):
    HydrogenBot.connect()
    HydrogenBot.authenticate()
    HydrogenBot.checkout_inbox()
    HydrogenBot.get_emails()
    HydrogenBot.read_emails()
    HydrogenBot.parse_emails()
