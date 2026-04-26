from django.db import models
from products.models import Product
from orders.models import Order

# Create your models here.

class Orderitem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    unit_price = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    subtotal = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    
    class Meta:
        unique_together = ('order', 'product')
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return f'{self.quantity} - {self.product.name}'