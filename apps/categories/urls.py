from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='categorias')

urlpatterns = [
    path('excluir/<int:id_category>/', views.delete_category, name='delete_category'),
    path('editar/<int:id_category>/', views.edit_category, name='edit_category'),
    path('listar/', views.list_categories, name='list_categories'),
    path('adicionar/', views.add_category, name='add_category'),
    path('', include(router.urls) ),
]