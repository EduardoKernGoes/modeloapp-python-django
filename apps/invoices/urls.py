from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'invoices'

router = routers.SimpleRouter()
router.register('', views.InvoiceViewSet, basename='notas')

urlpatterns = [
    path('', include(router.urls) )
]