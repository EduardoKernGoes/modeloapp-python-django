from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('produtos/', include('products.urls', namespace='products')),
    path('people/', include('people.urls', namespace='people')),
]
