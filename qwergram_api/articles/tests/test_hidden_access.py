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

    def create_articles(self):
        self.open_article = models.CodeArticleModel(
            title="A really informative blog post",
            content="Woah, amazing text! " * 100,
            draft=True,
            hidden=False,
        )
        self.hidden_article = models.CodeArticleModel(
            title="A very personal blog post",
            content="I @#%@ing hate %@#%!!! " * 100,
            draft=True,
            hidden=True,
        )
        self.open_article.save()
        self.hidden_article.save()

    def create_shares(self):
        self.open_share = models.RepostModel(
            title="Amazing article!",
            short_description="Very short description",
            link="http://www.example.com",
            hidden=False
        )
        self.hidden_share = models.RepostModel(
            title="Embarassing link",
            short_description="I need this for science",
            link="http://www.anime_for_weabs.com/very_weab_shtuff",
            hidden=True,
        )
        self.open_share.save()
        self.hidden_share.save()

    def create_stats(self):
        self.open_stat = models.StatModel(
            name="identity",
            value="""
            {
                "first_name": "Norton",
                "last_name": "Pengra",
                "age": 19,
            }
            """
        )
        self.hidden_stat = models.StatModel(
            name="secret_identity",
            value="""
            {
                "secret_identity": "Batman",
                "car": "Bat mobile"
            }
            """
        )
        self.open_stat.save()
        self.hidden_stat.save()

    def create_models(self):
        self.create_ideas()
        self.create_articles()
        self.create_shares()
        self.create_stats()

    def setUp(self):
        super(HiddenModelFactory, self).setUp()
        self.create_models()


class HiddenIdeasAPIAccessTest(HiddenModelFactory):

    idea_endpoint = '/api/v1/ideas/'

    @property
    def open_model_url(self):
        return self.idea_endpoint + str(self.open_idea.id) + '/'

    @property
    def hidden_model_url(self):
        return self.idea_endpoint + str(self.hidden_idea.id) + '/'

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


class HiddenArticlesAPIAccessTest(HiddenModelFactory):

    article_endpoint = '/api/v1/articles/'

    @property
    def open_model_url(self):
        return self.article_endpoint + str(self.open_article.id) + '/'

    @property
    def hidden_model_url(self):
        return self.article_endpoint + str(self.hidden_article.id) + '/'

    def test_article_access_hidden_unauth(self):
        response = self.client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_article_access_hidden_user(self):
        response = self.user_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_article_access_hidden_admin(self):
        response = self.admin_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 200)


class HiddenSharesAPIAccessTest(HiddenModelFactory):

    share_endpoint = '/api/v1/shares/'

    @property
    def open_model_url(self):
        return self.share_endpoint + str(self.open_share.id) + '/'

    @property
    def hidden_model_url(self):
        return self.share_endpoint + str(self.hidden_share.id) + '/'

    def test_share_access_hidden_unauth(self):
        response = self.client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_share_access_hidden_user(self):
        response = self.user_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_share_access_hidden_admin(self):
        response = self.admin_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 200)


class HiddenStatsAPIAccessTest(HiddenModelFactory):

    stat_endpoint = '/api/v1/stats/'

    @property
    def hidden_model_url(self):
        return self.stat_endpoint + str(self.hidden_stat.id) + '/'

    def test_stat_access_hidden_unauth(self):
        response = self.client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_stat_access_hidden_user(self):
        response = self.user_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 404)

    def test_stat_access_hidden_user(self):
        response = self.admin_client.get(self.hidden_model_url)
        self.assertEqual(response.status_code, 200)
