from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as authview
from articles import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'articles', views.CodeArticleViewSet)
router.register(r'ideas', views.PotentialIdeaViewSet)
router.register(r'shares', views.RepostViewSet)
router.register(r'repos', views.GithubViewSet)

urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'api-auth/token/', authview.obtain_auth_token),
    url(r'', include(router.urls)),
]
