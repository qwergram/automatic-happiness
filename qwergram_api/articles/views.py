from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from articles import models
from articles import serializers


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
    queryset = models.CodeArticleModel.objects.all()
    serializer_class = serializers.CodeArticleSerializer


class PotentialIdeaViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views PotentialIdea models."""
    queryset = models.PotentialIdeaModel.objects.all()
    serializer_class = serializers.PotentialIdeaSerializer


class RepostViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Repost models."""
    queryset = models.RepostModel.objects.all()
    serializer_class = serializers.RepostSerializer
