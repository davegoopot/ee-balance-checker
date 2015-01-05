"""
    Login to the https://web.orange.co.uk/ site and parse out the current
    balance.
"""

import requests

class EEConnector(object):
    """Connect to the website and get the raw page showing containing the
       balance information
    """

    def _fetch_login_page(self):
        """Fetch the login page and return the requests response object"""
        return requests.get('https://web.orange.co.uk/id/signin.php',
                            verify='SymantecClass3SecureServerCA-G4.crt')

