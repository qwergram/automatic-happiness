"""Read emails from $EMAIL_ADDR and post them to the api."""

import imaplib
import smtplib
import email
import requests
from requests.auth import HTTPBasicAuth


class Hydrogen(object):
    """
    Hydrogen Bot:
    A bot that reads my emails and saves the proper emails to the API endpoint.
    """

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
        self.admin_email = EMAIL_ADMIN

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
                # self.mail.copy(email_num, b'[Gmail]/Trash')
            self.raw_emails = True
        else:
            raise EnvironmentError('Fetch the emails first (Hydrogen.get_emails)')

    def parse_emails(self):
        if self.raw_emails:
            for i, message in enumerate(self.emails):
                parsed_email = {
                    'subject': message['Subject'],
                    'time': message['Date'],
                    'from': message['from'],
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
                ) and (
                    self.admin_email in message['from']
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


class Helium(Hydrogen):
    """
    Helium Bot:
    A bot that checks for replies to any emails that it's sent out.
    """

    def filter_emails(self):
        if self.parsed:
            emails = []
            for message in self.emails:
                if (
                    self.admin_email in message['from'] and
                    message['subject'].lower().startswith('article #') and
                    'delete' in message['content'].lower()
                ):
                    emails.append(message['title'].split('#', 1)[-1])
            self.emails = emails
            self.filtered = True
        else:
            raise EnvironmentError('Parse the emails first (Helium.parse_emails)')

    def run(self):
        self.connect()
        self.authenticate()
        self.checkout_inbox()
        self.get_emails()
        self.read_emails()
        self.parse_emails()
        self.filter_emails()

class Lithium(object):
    """
    Lithium Bot:
    A bot that takes the articles HydrogenBot spits out and then
    emails me in 24 hrs, asking for final approval before submitting them to
    the API with draft: False.
    """


    def __init__(self, articles):
        self.articles = articles
        self.email_queue = []
        self.local_endpoint = LOCAL_ENDPOINT
        self.public_endpoint = PUBLIC_ENDPOINT
        self.admin_name = ADMIN_USER.capitalize()

        self.admin_email = EMAIL_ADMIN
        self.email_addr = EMAIL_ADDR
        self.email_pass = EMAIL_PASS
        self.email_smtp = "{}:{}".format(EMAIL_HOST, EMAIL_PORT)

        self.wait_period = 24
        self.review_period = 12

    def submit_articles(self):
        for article in self.articles:
            email_queue = False
            if not article['draft']:
                email_queue = article['draft'] = True
            response = requests.post(
                self.local_endpoint + 'articles/',
                data=article,
                auth=HTTPBasicAuth(ADMIN_USER, ADMIN_PASS),
            )
            assert response.ok, response.json()
            if email_queue:
                self.email_queue.append(response.json())

    def send_emails(self):
        for email_content in self.email_queue:
            server = smtplib.SMTP(self.email_smtp)
            server.ehlo()
            server.starttls()
            server.login(self.email_addr, self.email_pass)
            server.sendmail(self.email_addr, self.admin_email, email_content)

    def format_emails(self):
        for i, article in enumerate(self.email_queue):
            email_contents = (
            "From: {from_addr}\r\n"
            "To: {to_addr}\r\n"
            "Subject: Article #{article_number}\r\n\r\n"
            "Hey {admin},\n\n"
            "About {wait_period} hours ago, you submitted an article ({title}). Due to company policy at "
            "Qwergram Entertainment Industries, we ask writers to review their work {wait_period} hours after "
            "submission. Below is what you wrote. Please review what you wrote, and if you still "
            "feel good about it, great! You can ignore this email and we'll publish your article "
            "in {review_period} hours. If you see anything you'd like to change, please reply to this email and "
            "we'll delete this article and you can always submit again.\n\n"
            "Here's the link where the article currently lives: {link}\n\n\n"
            "Thanks!\nHydrogen Bot & Lithium Bot\n\n\nThe article you wrote:\n\n{content}"
            ).format(
                from_addr=self.email_addr,
                to_addr=self.admin_email,
                article_number=article['url'].split('/')[-2],
                admin=self.admin_name,
                wait_period=self.wait_period,
                title=article['title'],
                review_period=self.review_period,
                link=article['url'].replace(self.local_endpoint, self.public_endpoint),
                content=article['content'],
            )
            self.email_queue[i] = email_contents

    def publish_articles(self):
        HBot = Helium(
            email_addr=self.email_addr,
            email_pass=self.email_pass,
            email_imap=self.email_imap,
        )
        HBot.run()
        print(HBot.emails)

if __name__ == "__main__":
    import os

    EMAIL_ADDR = os.environ['EMAIL_ADDR']
    EMAIL_PASS = os.environ['EMAIL_PASS']
    EMAIL_IMAP = os.environ['EMAIL_IMAP']
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = os.environ['EMAIL_PORT']
    EMAIL_ADMIN = os.environ['EMAIL_ADMIN']
    ADMIN_USER = os.environ['ADMIN_USER']
    ADMIN_PASS = os.environ['ADMIN_PASS']
    LOCAL_ENDPOINT = "http://127.0.0.1:8000/api/v1/"
    PUBLIC_ENDPOINT = "http://{}/api/v1/".format(os.environ['SERVER_LOCATION'])

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
    Bot2 = Lithium(Bot.emails)
    Bot2.submit_articles()
    Bot2.format_emails()
    Bot2.send_emails()
    Bot3 = Helium(
        email_addr=EMAIL_ADDR,
        email_pass=EMAIL_PASS,
        email_imap=EMAIL_IMAP,
    )
    Bot3.connect()
    Bot3.authenticate()
    Bot3.checkout_inbox()
    Bot3.get_emails()
    Bot3.read_emails()
    Bot3.parse_emails()
    Bot3.filter_emails()
