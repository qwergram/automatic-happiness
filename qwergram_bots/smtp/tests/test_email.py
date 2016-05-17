"""Read emails from $EMAIL_ADDR and post them to the api."""

import os
import imaplib
import email
import json
import requests
from requests.auth import HTTPBasicAuth

EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']
EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
ADMIN_USER = os.environ['ADMIN_USER']
ADMIN_PASS = os.environ['ADMIN_PASS']
LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"
