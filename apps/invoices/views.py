from django.shortcuts import render
from .models import Invoice
from rest_framework import viewsets
from .serializer import InvoiceSerializer

# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer