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

    users_endpoint = '/api/v1/users/'

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
