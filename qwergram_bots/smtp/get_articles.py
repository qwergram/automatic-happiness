"""Read emails from $EMAIL_ADDR and post them to the api."""

import os
import imaplib

EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']
EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
ADMIN_USER = os.environ['ADMIN_USER']
ADMIN_PASS = os.environ['ADMIN_PASS']
LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"

class Hydrogen(object):

    email_addr = EMAIL_ADDR
    email_pass = EMAIL_PASS

    def __init__(self):

        self.emails = []
        self.in_inbox = False
        self.opened_inbox = False

        self.create_email()
        self.authenticate()

    def create_email(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def authenticate(self):
        self.mail.login(self.email_addr, self.email_pass)

    def checkout_inbox(self):
        self.in_inbox = True
        self.mail.select('Inbox')

    def get_emails(self):
        if self.in_inbox:
            (status, emails) = self.mail.search(None, 'ALL')
            self.emails = emails[0].split(b' ')
        else:
            raise EnvironmentError('checkout the inbox first (Hydrogen.checkout_inbox)')

    def read_emails(self):
        if self.opened_inbox:
            (rv, data) = self.mail.fetch(email_num, '(RFC822)')
        else:
            raise EnvironmentError('Fetch the emails first (Hydrogen.get_emails)')


if __name__ == "__main__":
    Bot = Hydrogen()
    Bot.checkout_inbox()
    # Bot.get_emails()
    Bot.read_emails()
