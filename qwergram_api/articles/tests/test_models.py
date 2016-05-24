from django.test import TestCase, Client
from django.contrib.auth.models import User
from articles.tests.test_permissions import UserFactory
from articles import models


class HiddenModelFactory(UserFactory):

    def create_ideas(self):
        self.open_idea = models.PotentialIdeaModel(
            title="A crazy Idea",
            pitch="But with great potential",
            priority=1,
            hidden=False,
        )
        self.hidden_idea = models.PotentialIdeaModel(
            title="A money making Idea",
            pitch="Details of the master plan",
            priority=100,
            hidden=True,
        )
        self.open_idea.save()
        self.hidden_idea.save()

    def create_models(self):
        self.create_ideas()

    def setUp(self):
        super(HiddenIdeasAPIAccessTest, self).setUp()
        self.create_models()


class HiddenIdeasAPIAccessTest(HiddenModelFactory):

    idea_endpoint = '/api/v1/ideas/'

    @property
    def open_model_url(self):
        return self.idea_endpoint + str(self.open_model.id) + '/'

    @property
    def hidden_model_url(self):
        return self.idea_endpoint + str(self.hidden_model.id) + '/'

    # Theoretically, these tests are covered articles.tests.test_permission
    # def test_idea_access_open_unauth(self):
    #     response = self.client.get(self.open_model_url)
    #     self.assertEqual(response.status_code, 200)

    def test_idea_access_hidden_unauth(self):
        response = self.client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_idea_access_hidden_user(self):
        response = self.user_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_idea_access_hidden_admin(self):
        response = self.admin_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 200)
