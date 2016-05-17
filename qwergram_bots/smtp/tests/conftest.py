"""Test Hydrogen mockers"""
import pytest
from smtp.get_articles import Hydrogen

class OfflineHydrogen(Hydrogen):

    email_addr = "test@test.com"
    email_pass = "amazing_password1"
    email_imap = "imap.totally_valid_server.net"

    def connect(self):
        self.connected = True
        self.mail = object

@pytest.fixture
def HydrogenBot():
    return OfflineHydrogen()
