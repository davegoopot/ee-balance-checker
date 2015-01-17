import unittest
from ee_balance import *


class EEUnitTests(unittest.TestCase):
    def setUp(self):
        self.eecon = EEConnector(username='07583767812', password='xW7QMsMG48')
        
    def test_fetch_login_page(self):
        login_page_response = self.eecon._fetch_login_page()
        self.assertEqual(200, login_page_response.status_code)
        
    # def test_fetch_balance_page(self):
        # balance_page_response = self.eecon._fetch_balance_page()
        # self.assertEqual(200, balance_page_response.status_code)

        