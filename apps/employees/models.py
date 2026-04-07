from django.db import models
from people.models import Person

# Create your models here.

class Employee(Person):
    salary = models.DecimalField('Salário', max_digits=10, decimal_places=2, default=0)
    position = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering =['id']

    def __str__(self):
        return super().__str__()