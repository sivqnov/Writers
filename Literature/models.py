from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55, verbose_name='Имя')
    alias = models.CharField(max_length=55, verbose_name='Псевдоним')