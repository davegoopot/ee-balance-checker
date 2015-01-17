"""
    Login to the https://web.orange.co.uk/ site and parse out the current
    balance.
"""

import requests

class EEConnector(object):
    """Connect to the website and get the raw page showing containing the
       balance information
    """
    
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
        