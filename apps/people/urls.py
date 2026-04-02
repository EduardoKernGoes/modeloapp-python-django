from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'people'

router = routers.SimpleRouter()
router.register('', views.PersonViewSet, basename='people')

urlpatterns = [
    path('', include(router.urls))
]