"""Test Hydrogen mockers"""
import pytest
from smtp.get_articles import Hydrogen

class OfflineHydrogen(Hydrogen):

    def connect(self):
        self.connected = True
        self.mail = object

@pytest.fixture
def HydrogenBot():
    return OfflineHydrogen()
