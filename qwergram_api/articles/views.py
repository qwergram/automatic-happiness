from rest_framework import viewsets, permissions, views, response, status
from django.contrib.auth.models import User, Group
from articles import models
from articles import serializers
from articles.permissions import IsAdminOrReadOnly
import sys
import os
import requests

# Import bots here
hbot_loc = __file__.split('qwergram_api')[0] + 'qwergram_bots/github/'
bbot_loc = __file__.split('qwergram_api')[0] + 'qwergram_bots/twitter/'
sys.path.append(hbot_loc)
sys.path.append(bbot_loc)

from helium_bot import GITHUB_ENDPOINT, Helium
from beryllium_bot import (
    Beryllium,
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_SECRET,
)
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views User models."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Group models."""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (permissions.IsAdminUser, )


class CodeArticleViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views CodeArticle models."""
    serializer_class = serializers.CodeArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )

    # queryset is required to be defined due to a bug in django_rest_framework
    # https://github.com/tomchristie/django-rest-framework/issues/933
    queryset = models.CodeArticleModel.objects.filter(pk=-1)
    def get_queryset(self):
        if self.request.user.is_staff and self.request.user.is_superuser:
            return models.CodeArticleModel.objects.all().order_by('-last_modified')
        return models.CodeArticleModel.objects.filter(hidden=False).order_by('-last_modified')


class PotentialIdeaViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views PotentialIdea models."""
    serializer_class = serializers.PotentialIdeaSerializer
    permission_classes = (IsAdminOrReadOnly, )

    # queryset is required to be defined due to a bug in django_rest_framework
    # https://github.com/tomchristie/django-rest-framework/issues/933
    queryset = models.PotentialIdeaModel.objects.filter(pk=-1)
    def get_queryset(self):
        if self.request.user.is_staff and self.request.user.is_superuser:
            return models.PotentialIdeaModel.objects.all().order_by('-date_created')
        return models.PotentialIdeaModel.objects.filter(hidden=False).order_by('-date_created')



class RepostViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Repost models."""
    serializer_class = serializers.RepostSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        """
        Override the CreateModelMixin.perform_create method and insert our own.
        We want to tweet the share. So let's do it here.

        Theoretically, we could do this with signals. But I'm not sure what the
        best practice, so I'm going with what makes the most sense/easiest.
        """
        # This is cleaner than super()...
        # Copied from rest_framework.mixins.CreateModelMixin.perform_create
        serializer.save()

        tweet_text = "".join([
            serializer.data['short_description'],
            " (", serializer.data['link'], ")"
        ])
        BerylliumBot = Beryllium(
            CONSUMER_KEY,
            CONSUMER_SECRET,
            ACCESS_TOKEN,
            ACCESS_SECRET,
        )
        BerylliumBot.verify_credentials()
        BerylliumBot.tweet(tweet_text)

    # queryset is required to be defined due to a bug in django_rest_framework
    # https://github.com/tomchristie/django-rest-framework/issues/933
    queryset = models.RepostModel.objects.filter(pk=-1)
    def get_queryset(self):
        if self.request.user.is_staff and self.request.user.is_superuser:
            return models.RepostModel.objects.all().order_by('-date_posted')
        return models.RepostModel.objects.filter(hidden=False).order_by('-date_posted')



class GithubViewSet(views.APIView):
    """API endpoint that views Github models."""
    permission_classes = (IsAdminOrReadOnly, )
    github_endpoint = GITHUB_ENDPOINT

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        Bot = Helium(self.github_endpoint)
        # In case you run the commented out tests offline
        try:
            Bot.get_repos()
        except requests.exceptions.ConnectionError:
            Bot.ready_for_local = True
            Bot.repos = [{
                "id": None,
                "clone_url": None,
                "commits_url": None,
                "created_at": None,
                "description": None,
                "full_name": None,
                "homepage": None,
                "html_url": None,
                "open_issues": None,
                "pushed_at": None,
                "size": None,
                "updated_at": None,
                "watchers": None,
                "language": None,
            }]
        Bot.simplify_data()
        return response.Response(Bot.repos, status=status.HTTP_200_OK)
