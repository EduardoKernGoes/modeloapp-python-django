from django.db import models
from orders.models import Order

# Create your models here.

class Invoice(models.Model):
    number = models.CharField('Numero', max_length=100)
    issue_date = models.DateField('Data de emissão', auto_now=False, auto_now_add=False) 
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='invoice')

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering =['id']

    def __str__(self):
        return f'{self.number}'