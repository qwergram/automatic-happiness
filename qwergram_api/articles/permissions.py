from rest_framework.permissions import BasePermission, SAFE_METHODS
# Create your permissions here.

class IsAdminOrReadOnly(BasePermission):
    """
    Read permission for everyone. Only admins can modify content.
    Code from https://libraries.io/github/maykinmedia/django-rest-framework-proxy#permissions
    """
    def has_permission(self, request, view, obj=None):
        return (request.method in SAFE_METHODS or request.user and request.user.is_staff)
