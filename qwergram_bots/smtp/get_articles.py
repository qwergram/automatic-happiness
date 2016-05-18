"""Read emails from $EMAIL_ADDR and post them to the api."""

import imaplib
import email


class Hydrogen(object):

    def __init__(self, email_addr, email_pass, email_imap):

        self.emails = []
        self.in_inbox = False
        self.opened_inbox = False
        self.authenticated = False
        self.connected = False
        self.raw_emails = False
        self.parsed = False

        self.email_addr = email_addr
        self.email_pass = email_pass
        self.email_imap = email_imap

    def connect(self):
        self.connected = True
        self.mail = imaplib.IMAP4_SSL(self.email_imap)

    def authenticate(self):
        if self.connected:
            self.authenticated = True
            self.mail.login(self.email_addr, self.email_pass)
        else:
            raise EnvironmentError("Connect to the server first (Hydrogen.connect)")

    def checkout_inbox(self):
        if self.authenticated:
            self.in_inbox = True
            self.mail.select('Inbox')
        else:
            raise EnvironmentError('Authenticate first (Hydrogen.authenticate)')

    def get_emails(self):
        if self.in_inbox:
            (status, emails) = self.mail.search(None, 'ALL')
            self.emails = emails[0].split(b' ')
            self.opened_inbox = True
        else:
            raise EnvironmentError('Checkout the inbox first (Hydrogen.checkout_inbox)')

    def read_emails(self):
        if self.opened_inbox:
            for i, email_num in enumerate(self.emails):
                (rv, data) = self.mail.fetch(email_num, '(RFC822)')
                self.emails[i] = email.message_from_string(data[0][1].decode())
            self.raw_emails = True
        else:
            raise EnvironmentError('Fetch the emails first (Hydrogen.get_emails)')

    def parse_emails(self):
        if self.raw_emails:
            for i, message in enumerate(self.emails):
                parsed_email = {
                    'subject': message['Subject'],
                    'time': message['Date'],
                    'content': str(message.get_payload()[0]).split('\n\n', 1)[1].replace('\n', ' ')
                }
                self.emails[i] = parsed_email
            self.parsed = True
        else:
            raise EnvironmentError('Read the emails first (Hydrogen.read_emails)')

    def filter_emails(self):
        if self.parsed:
            emails = []
            for message in self.emails:
                if (
                    message['subject'].endswith('.article.txt') or
                    message['subject'].endswith('.draft.txt')
                ):
                    emails.append({
                        "title": message['subject'].replace('.article.txt', '').replace('.draft.txt', ''),
                        "content": message['content'].replace('\r', ''),
                        "draft": message['subject'].endswith('draft.txt'),
                        "original_idea": None,
                    })
            self.filtered = True
            self.emails = emails
        else:
            raise EnvironmentError('Parse the emails first (Hydrogen.parse_emails)')

if __name__ == "__main__":
    import os

    EMAIL_ADDR = os.environ['EMAIL_ADDR']
    EMAIL_PASS = os.environ['EMAIL_PASS']
    EMAIL_IMAP = os.environ['EMAIL_IMAP']
    EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
    ADMIN_USER = os.environ['ADMIN_USER']
    ADMIN_PASS = os.environ['ADMIN_PASS']
    LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"

    Bot = Hydrogen(
        email_addr=EMAIL_ADDR,
        email_pass=EMAIL_PASS,
        email_imap=EMAIL_IMAP,
    )
    Bot.connect()
    Bot.authenticate()
    Bot.checkout_inbox()
    Bot.get_emails()
    Bot.read_emails()
    Bot.parse_emails()
    Bot.filter_emails()
    print(Bot.emails)
