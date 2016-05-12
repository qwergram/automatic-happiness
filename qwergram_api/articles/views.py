from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from articles import models
from articles import serializers

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views User models."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Group models."""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class CodeArticleViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views CodeArticle models."""
    queryset = models.CodeArticleModel.objects.all()
    serializer_class = serializers.CodeArticleSerializer
