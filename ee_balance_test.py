import configparser
import unittest
from ee_balance import *


class EEUnitTests(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read('secret.auth')
        self.eecon = EEConnector(username=config['auth']['username'], password=config['auth']['password'])
        
    def test_fetch_login_page(self):
        login_page_response = self.eecon._fetch_login_page()
        self.assertEqual(200, login_page_response.status_code)
        
    def test_fetch_balance_page(self):
        balance_page_response = self.eecon._fetch_balance_page()
        self.assertEqual(200, balance_page_response.status_code)

        