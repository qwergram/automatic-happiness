"""Read emails from $EMAIL_ADDR and post them to the api."""

import os
import sys
import imaplib
import email
import datetime
import json
import requests


EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_IMAP = os.environ['EMAIL_IMAP']
EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"

class EmailClient(object):

    idea_endpoint = LOCAL_ENDPOINT + "ideas/"
    share_endpoint = LOCAL_ENDPOINT + "shares/"
    article_endpoint = LOCAL_ENDPOINT + "articles/"

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
                json_data = self.verify_email(message)
                if json_data:
                    self.save_json_data(json_data)
            self.mail.copy(email_num, b'[Gmail]/Trash')

    def save_json_data(self, json_data):
        submission_type = json_data['type']
        return getattr("submit_" + submission_type)(json_data)

    def submit_idea(self, json_data):
        return requests.post(
            self.idea_endpoint,
            data={
                "title": json_data['title'],
                "pitch": json_data['pitch'],
                "priority": json_data['priority'],
            }
        )

    def submit_share(self, json_data):
        pass

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
            json_data = {key.strip(): val.strip() for key, val in sjson}
        if data_type == 'json':
            json_data = self.get_json_from_payload(message)
        for key, value in json_data.items():
            del json_data[key]
            json_data[key.lower()] = value
        return json_data

    def validify_idea(self, data_type, message):
        json_data = self.convert_to_json(data_type, message)
        if {key.lower() for key in json_data.keys()} == {'title', 'pitch', 'priority'}:
            return json_data
        return False

    def validify_share(self, data_type, message):
        json_data = self.convert_to_json(data_type, message)
        if {key.lower() for key in json_data.keys()} == {'title', 'short_description', 'url'}:
            return json_data
        return False

    def verify_email(self, message):
        submission_type, data_type = message['Subject'].split('.')
        from_addr = message['from']
        time_sent = message['Date']
        is_admin = EMAIL_ADMIN in from_addr
        try:
            if is_admin:
                json_data = getattr(self, "validify_" + submission_type.lower())(data_type, message)
                if json_data:
                    json_data['time'] = time_sent
                    json_data['type'] = submission_type.lower()
                    print(json.dumps(json_data, indent=2))
                    return json_data
        except AttributeError:
            pass
        return False

    def is_valid_email(self, subject):
        try:
            submission_type, data_type = subject.split('.')
            return (
                submission_type.lower() in ['idea', 'share', 'article'] and
                data_type.lower() in ['json', 'sjson']
            )
        except (ValueError):
            return False

    def close(self):
        import pdb; pdb.set_trace()
        self.mail.logout()

if __name__ == "__main__":
    print("Grabbing emails")
    E = EmailClient()
    E.checkout_inbox()
    E.get_email_list()
    E.close()
