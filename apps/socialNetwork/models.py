from django.db import models

# Create your models here.

class SocialNetwork(models.Model):
    name = models.CharField('Nome', max_length=100)
    content_type = models.TextField('Tipo de Conteúdo', max_length=100)
    url = models.URLField('URL', max_length=255)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'