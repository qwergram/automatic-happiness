from django.contrib.auth.models import User, Group
from rest_framework import serializers
from articles import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the user model."""
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the group model."""
    class Meta:
        model = Group
        fields = ('url', 'name')


class CodeArticleSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Code Article model."""
    class Meta:
        model = models.CodeArticleModel
        exclude = []


class PotentialIdeaSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Potential Idea model."""
    class Meta:
        model = models.PotentialIdeaModel
        exclude = []


class RepostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Repost model."""
    class Meta:
        model = models.RepostModel
        exclude = []


class GithubSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Github Repos."""
    clone_url = serializers.URLField()
    commits_url = serializers.URLField()
    created_at = serializers.DateTimeField()  # iso-8601 format
    description = serializers.CharField()
    home_page = serializers.URLField()
    html_url = serializers.URLField()
    language = serializers.CharField()
    open_issues = serializers.IntegerField()
    pushed_at = serializers.DateTimeField()
    size = serializers.IntegerField()
    updated_at = serializers.DateTimeField()
    watchers = serializers.IntegerField()
