"""
    TODO:  Refactor out EEConnector to set up
"""

import unittest
from ee_balance import *


class EEUnitTests(unittest.TestCase):
    def setUp(self):
        self.eecon = EEConnector()
        
    def test_fetch_login_page(self):
        login_page_response = self.eecon._fetch_login_page()
        self.assertEqual(200, login_page_response.status_code)
        
    