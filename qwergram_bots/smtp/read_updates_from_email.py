"""Read emails from $EMAIL_ADDR and post them to the api."""

import os
import sys
import imaplib
import email
import datetime
import json


EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']
EMAIL_ADMIN = os.environ['EMAIL_ADMIN']


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

    def checkout_inbox(self):
        self.mail.select('Inbox')

    def get_email_list(self):
        status, emails = self.mail.search(None, 'ALL')
        self.read_emails(emails)

    def read_emails(self, emails):
        for email_num in emails[0].split():
            (rv, data) = self.mail.fetch(email_num, '(RFC822)')
            message = email.message_from_string(data[0][1].decode())
            subject = message['Subject']
            if self.is_valid_email(subject):
                self.verify_email(message)

    def get_json_from_payload(self, message):
        payload = str(message.get_payload()[0])
        return json.loads(payload.split('\n\n')[1].replace('\n', ' '))

    def convert_to_json(self, data_type, message):
        if data_type == 'sjson':
            # TODO: Should be wrapped in a try-except block, but for debbuging
            # purposes I'll leave it be.
            message_text = str(message.get_payload()[0])
            message_text = message_text.split('\n\n')[1]
            sjson = message_text.split(';')
            sjson = filter(lambda x: x.strip() != '', sjson)
            sjson = [val.replace('\n', ' ').strip().split('..', 1) for val in sjson]
            sjson = {key.strip(): val.strip() for key, val in sjson}
            json_data = sjson
        if data_type == 'json':
            json_data = self.get_json_from_payload(message)
        return json_data

    def validify_idea(self, data_type, message):
        json_data = self.convert_to_json(data_type, message)
        if set(json_data.keys()) == {'title', 'pitch', 'priority'}:
            return json_data
        return False

    def validify_share(self, data_type, message):
        json_data = self.convert_to_json(data_type, message)
        if set(json_data.keys()) == {'title', 'short_description', 'url'}:
            return json_data
        return False

    def verify_email(self, message):
        submission_type, data_type = message['Subject'].split('.')
        from_addr = message['from']
        time_sent = message['Date']
        is_admin = EMAIL_ADMIN in from_addr
        if is_admin:
            json_data = getattr(self, "validify_" + submission_type)(data_type, message)
            if json_data:
                json_data['time'] = time_sent
                print(json.dumps(json_data, indent=2))
                return json_data
        return False

    def is_valid_email(self, subject):
        try:
            submission_type, data_type = subject.split('.')
            return (
                submission_type in ['idea', 'share', 'article'] and
                data_type in ['json', 'sjson']
            )
        except (ValueError):
            return False

    def close(self):
        self.mail.logout()

if __name__ == "__main__":
    print("Grabbing emails")
    E = EmailClient()
    E.checkout_inbox()
    E.get_email_list()
    E.close()
