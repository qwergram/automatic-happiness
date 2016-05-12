from django.conf.urls import url, include
from rest_framework import routers
from articles import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'articles', views.CodeArticleViewSet)

urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'', include(router.urls)),
]
