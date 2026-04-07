from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('produtos/', include('products.urls', namespace='products')),
    path('pessoas/', include('people.urls', namespace='people')),
    path('redesSociais/', include('socialNetwork.urls', namespace='socialNetwork')),
    path('funcionarios/', include('employees.urls', namespace='employees')),
]
