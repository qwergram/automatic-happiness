from django.test import TestCase, Client
from django.contrib.auth.models import User

class UserFactory(TestCase):

    login_endpoint = '/api/v1/api-auth/login/'

    def create_titan(self):

        titan = User(
            username='titan',
            email='titan@destiny.com',
            first_name='titan',
            last_name='lastname'
        )
        titan.set_password('password1')
        titan.save()
        return titan

    def create_admin(self):
        admin = User(
            username='admin',
            email='admin@thissite.com',
            first_name='jon',
            last_name='doe',
            is_staff=True,
            is_superuser=True,
        )
        admin.set_password('password')
        admin.save()
        return admin

    def setUp(self):
        self.create_titan()
        self.create_admin()

        self.admin_client = Client()
        self.user_client = Client()
        self.client = Client()

        self.login_okay = self.user_client.post(
            self.login_endpoint,
            {
                'username': 'titan',
                'password': 'password1',

            }
        )
        self.bad_login = self.user_client.post(
            self.login_endpoint,
            {
                'username': 'whoami',
                'password': 'a password',

            }
        )
        self.admin_login = self.admin_client.post(
            self.login_endpoint,
            {
                'username': 'admin',
                'password': 'password',
            }
        )

    def test_login_okay(self):
        self.assertEquals(self.login_okay.status_code, 302)

    def test_bad_login_fails(self):
        self.assertContains(self.bad_login, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_admin_login_okay(self):
        self.assertEquals(self.login_okay.status_code, 302)


class UserAPIAccessTest(UserFactory):

    user_endpoint = '/api/v1/users/'
    post_example = {
        "username": "another_user",
        "email": "auser@aservice.com",
        "groups": [],
    }

    def test_users_access_admin(self):
        response = self.admin_client.get(self.user_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_users_access_user(self):
        response = self.user_client.get(self.user_endpoint)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'You do not have permission to perform this action.')

    def test_users_access_unauth(self):
        response = self.client.get(self.user_endpoint)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'Authentication credentials were not provided.')

    def test_users_create_admin(self):
        response = self.admin_client.post(self.user_endpoint, self.post_example)
        self.assertEquals(response.status_code, 201)

    def test_users_create_user(self):
        response = self.user_client.post(self.user_endpoint, self.post_example)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'You do not have permission to perform this action.')

    def test_users_create_unauth(self):
        response = self.client.post(self.user_endpoint, self.post_example)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'Authentication credentials were not provided.')


class GroupAPIAccessTest(UserFactory):

    group_endpoint = '/api/v1/groups/'

    def test_groups_access_admin(self):
        response = self.admin_client.get(self.group_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_groups_access_group(self):
        response = self.user_client.get(self.group_endpoint)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'You do not have permission to perform this action.')

    def test_groups_access_unauth(self):
        response = self.client.get(self.group_endpoint)
        self.assertEquals(response.status_code, 403)
        self.assertEquals(response.json()['detail'], 'Authentication credentials were not provided.')


class ArticlesAPIAccessTest(UserFactory):

    article_endpoint = '/api/v1/articles/'

    def test_articles_access_admin(self):
        response = self.admin_client.get(self.article_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_articles_access_article(self):
        response = self.user_client.get(self.article_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_articles_access_unauth(self):
        response = self.client.get(self.article_endpoint)
        self.assertEquals(response.status_code, 200)


class IdeasAPIAccessTest(UserFactory):

    idea_endpoint = '/api/v1/ideas/'

    def test_ideas_access_admin(self):
        response = self.admin_client.get(self.idea_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_ideas_access_idea(self):
        response = self.user_client.get(self.idea_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_ideas_access_unauth(self):
        response = self.client.get(self.idea_endpoint)
        self.assertEquals(response.status_code, 200)


class SharesAPIAccessTest(UserFactory):

    share_endpoint = '/api/v1/shares/'

    def test_shares_access_admin(self):
        response = self.admin_client.get(self.share_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_shares_access_share(self):
        response = self.user_client.get(self.share_endpoint)
        self.assertEquals(response.status_code, 200)

    def test_shares_access_unauth(self):
        response = self.client.get(self.share_endpoint)
        self.assertEquals(response.status_code, 200)
