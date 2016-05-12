from rest_framework import viewsets
from articles.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views User models."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that edits/views Group models."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
