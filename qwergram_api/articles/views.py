from rest_framework import viewsets, permissions, views, response, status
from django.contrib.auth.models import User, Group
from articles import models
from articles import serializers
from articles.permissions import IsAdminOrReadOnly

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
    queryset = models.CodeArticleModel.objects.all().order_by('-last_modified')
    serializer_class = serializers.CodeArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )


class PotentialIdeaViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views PotentialIdea models."""
    queryset = models.PotentialIdeaModel.objects.all().order_by('-date_created')
    serializer_class = serializers.PotentialIdeaSerializer
    permission_classes = (IsAdminOrReadOnly, )


class RepostViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Repost models."""
    queryset = models.RepostModel.objects.all().order_by('-date_posted')
    serializer_class = serializers.RepostSerializer
    permission_classes = (IsAdminOrReadOnly, )


class GithubViewSet(views.APIView):
    """API endpoint that views Github models."""
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = []
        return response.Response(usernames, status=status.HTTP_200_OK)
