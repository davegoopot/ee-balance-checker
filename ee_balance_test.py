import unittest
from ee_balance import *

class EEUnitTests(unittest.TestCase):
    def test_instance_create(self):
        ee = EEConnector()
        