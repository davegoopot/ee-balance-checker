"""
    TODO:  Refactor out EEConnector to set up
"""

import unittest
from ee_balance import *


class EEUnitTests(unittest.TestCase):
    def test_instance_create(self):
        ee = EEConnector()
        
    def test_fetch_login_page(self):
        eecon = EEConnector()
        login_page_response = eecon._fetch_login_page()
        self.assertEqual(200, login_page_response.status_code)