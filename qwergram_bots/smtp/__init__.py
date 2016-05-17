import os

# Bot information for Qwergram Package Manager (QPM)
__APIVERSION__ = "v1"
__BOTNAME__ = "map_bot"
__BOTVERSION__ = "v2"
__DEPENDENCIES__ = []
__DOCS__ = """

This is a package for reading emails that I send to a specified email address
and then publishing them to the aws instance.

"""

# Globals that need to be defined
EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']
EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
ADMIN_USER = os.environ['ADMIN_USER']
ADMIN_PASS = os.environ['ADMIN_PASS']
LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/{api_ver}/".format(__APIVERSION__)
