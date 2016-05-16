"""Read emails from $EMAIL_ADDR and post them to the api."""

import os
import sys
import imaplib
import email
import datetime


EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']


class EmailClient(object):

    def __init__(self):
        self.email_addr = EMAIL_ADDR
        self.email_pass = EMAIL_PASS
        self.email_imap = EMAIL_IMAP
        self.create_email()
        self.authenticate()

    def create_email(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def authenticate(self):
        self.mail.login(EMAIL_ADDR, EMAIL_PASS)

    def close(self):
        self.mail.logout()

if __name__ == "__main__":
    print("Grabbing emails")
    E = EmailClient()
    E.close()
