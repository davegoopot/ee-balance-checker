"""
    Login to the https://web.orange.co.uk/ site and parse out the current
    balance.
"""

import configparser
import requests

class EEConnector(object):
    """Connect to the website and get the raw page showing containing the
       balance information
    """
    
    @staticmethod
    def construct_from_config_file(filename="secret.auth"):
        """Set up the instance from the config in the passed file"""
        config = ""
        with open(filename, "r") as f:
            config = f.read()
        return EEConnector.construct_from_config(config)
    
    @staticmethod
    def construct_from_config(config_data):
        """Set up the instance using the passed config data in ConfigParser format"""
        config = configparser.ConfigParser()
        config.read_string(config_data)
        return EEConnector(config['auth']['username'], config['auth']['password'])
        
    
    def __init__(self, username, password):
        """Record the authentication data in the format needed to login to ee"""
        self.authentication_data = {'LOGIN': username, 'PASSWORD': password}
        self.session = requests.Session()
        self.session.verify = 'SymantecClass3SecureServerCA-G4.crt'
        
    def _fetch_login_page(self):
        """Fetch the login page and return the requests response object"""
        return self.session.get('https://web.orange.co.uk/id/signin.php')
        

    def _fetch_balance_page(self):
        """Fetch the balance page and return the requests response object"""
        return self.session.post('https://web.orange.co.uk/id/signin.php?rm=StandardSubmit',
                                data=self.authentication_data,
                                allow_redirects=True)
        
    def _fetch_balance_json(self):
        """After login request the json that will state the balance"""
        return self.session.post('https://www.youraccount.orange.co.uk/sss/ajaxServices/plans/PAYGPlanDetails',
                                data=self.authentication_data,
                                allow_redirects=True)