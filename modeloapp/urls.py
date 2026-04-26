from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('token-autenticacao/', obtain_auth_token),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('produtos/', include('products.urls', namespace='products')),
    path('pessoas/', include('people.urls', namespace='people')),
    path('redes_sociais/', include('socialNetwork.urls', namespace='socialNetwork')),
    path('funcionarios/', include('employees.urls', namespace='employees')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('itens_pedido/', include('orderitems.urls', namespace='orderitems')),
    path('notas/', include('invoices.urls', namespace='invoices')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)