"""Test Hydrogen mockers"""
import pytest
from smtp.get_articles import Hydrogen


class MockMail(object):

    def __init__(self):
        self.login_count = 0

    def login(self, email_addr, email_pass):
        self.login_count += 1
        return True


class OfflineHydrogen(Hydrogen):


    def connect(self):
        self.connected = True
        self.mail = MockMail()

@pytest.fixture
def HydrogenBot():
    return OfflineHydrogen(
        email_addr="test@test.com",
        email_pass="amazing_password1",
        email_imap="imap.totally_valid_server.net",
    )
