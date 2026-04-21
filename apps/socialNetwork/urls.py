from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialNetwork'

router = routers.SimpleRouter()
router.register('', views.SocialNetworkViewSet, basename='redeSocial')

urlpatterns = [
    path('listar/', views.list_socialnetworks, name='list_socialnetworks'),
    path('adicionar/', views.add_socialnetwork, name='add_socialnetwork'),
    path('editar/<int:id_socialnetwork>/', views.edit_socialnetwork, name='edit_socialnetwork'),
    path('excluir/<int:id_socialnetwork>/', views.delete_socialnetwork, name='delete_socialnetwork'),
    path('', include(router.urls) )
]