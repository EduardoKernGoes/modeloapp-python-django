from django.db import models
from clients.models import Client
from employees.models import Employee

# Create your models here.

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField('Forma de Pagamento', max_length=30, choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('Cartao de Debito', 'Cartao de Debito'),
        ('pix', 'PIX'),
    ])
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    total = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return "%s" %(self.id)