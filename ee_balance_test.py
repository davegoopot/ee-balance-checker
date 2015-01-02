import unittest
from ee_balance import EEBalanceChecker

class EEUnitTests(unittest.TestCase):
    def test_instance_create(self):
        ee = EEBalanceChecker()
        