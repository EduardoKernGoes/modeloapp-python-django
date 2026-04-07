from django.db import models
from people.models import Person
from socialNetwork.models import SocialNetwork

# Create your models here.

class Client(Person):
    gender = models.CharField('Genero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    socialnetwork = models.ManyToManyField(SocialNetwork, verbose_name="Redes Socias")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return super().__str__()