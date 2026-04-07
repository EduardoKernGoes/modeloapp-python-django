from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialNetwork'

router = routers.SimpleRouter()
router.register('', views.SocialNetworkViewSet, basename='redeSocial')

urlpatterns = [
    path('', include(router.urls) )
]