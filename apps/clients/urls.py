from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.SimpleRouter()
router.register('', views.ClientViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls) )
]