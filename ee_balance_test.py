import unittest
from ee_balance import *


class EEUnitTests(unittest.TestCase):
    def setUp(self):
        self.eecon = EEConnector.construct_from_config_file()
        
    def test_fetch_login_page(self):
        login_page_response = self.eecon._fetch_login_page()
        self.assertEqual(200, login_page_response.status_code)
    
    def test_fetch_balance_json(self):
        balance_page_response = self.eecon._fetch_balance_page()
        self.assertEqual(200, balance_page_response.status_code)
        balance_json_response = self.eecon._fetch_balance_json()
        self.assertEqual(200, balance_json_response.status_code)

    def test_start_session_from_config_file(self):
        test_file_contents = """[auth]
username=uname
password=pword
"""
        eeconnector = EEConnector.construct_from_config(test_file_contents)
        self.assertEqual("uname", eeconnector.authentication_data['LOGIN'])
        self.assertEqual("pword", eeconnector.authentication_data['PASSWORD'])
        
        