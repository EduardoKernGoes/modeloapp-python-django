from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orders'

router = routers.SimpleRouter()
router.register('', views.OrderViewSet, basename='pedidos')

urlpatterns = [
    path('itens/', views.list_items_products, name='list_items_products'),
    path('carrinho/', views.cart, name='cart'),
    path('carrinho/adicionar/<int:product_id>/', views.add_cart, name='add_cart'),
    path('carrinho/editar/<int:product_id>/', views.edit_cart, name='edit_cart'),
    path('carrinho/excluir/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('listar/', views.list_orders, name='list_orders'),
    path('itens/<int:order_id>/', views.view_order, name='view_order'),
    path('itens/<int:order_id>/cancelar/', views.cancel_order, name='cancel_order'),
    #path('adicionar/', views.add_order, name='add_order'),
    path('', include(router.urls) )
]