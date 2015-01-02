ee-balance-checker
==================

Code to automatically check the balance on a EE pay-as-you-go account in the UK.

Commands
--------

 * run.sh -- fires up a docker image to run the dev environment.  /code in the docker image is mapped to the root of the git module directory on the host

Usage
-----

 python ee_balance.py [phone#] [password]
 
This will return the current balance remaining for the specified account.