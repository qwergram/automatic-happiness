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


class StatSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Stats model."""
    class Meta:
        model = models.StatModel
        exclude = []

    value = serializers.JSONField()
