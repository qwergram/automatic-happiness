from django.test import TestCase, Client
from articles import views


class UserFactory(TestCase):

    def setUp(self):

        from django.contrib.auth.models import User
        titan = User(
            username='titan',
            email='titan@destiny.com',
            first_name='titan',
            last_name='lastname'
        )
        titan.set_password('password1')


        admin = User(
            username='admin',
            email='admin@thissite.com',
            first_name='jon',
            last_name='doe',
            is_staff=True,
            is_superuser=True,
        )
        admin.set_password('password')

        titan.save()
        admin.save()

        self.admin_client = Client()
        self.user_client = Client()
        self.client = Client()

        self.login_okay = self.user_client.post(
            '/api/v1/api-auth/login/',
            {
                'username': 'titan',
                'password': 'password1',

            }
        )
        self.bad_login = self.user_client.post(
            '/api/v1/api-auth/login/',
            {
                'username': 'whoami',
                'password': 'a password',

            }
        )
        self.admin_login = self.admin_client.post(
            '/api/v1/api-auth/login/',
            {
                'username': 'admin',
                'password': 'password',
            }
        )


class UserLoginTestCase(UserFactory):

    def test_login_okay(self):
        self.assertEquals(self.login_okay.status_code, 302)

    def test_bad_login_fails(self):
        self.assertContains(self.bad_login, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_admin_login_okay(self):
        self.assertEquals(self.login_okay.status_code, 302)


# class UserAPIAccess(UserFactory):

    # def test_users_access_admin(self):
