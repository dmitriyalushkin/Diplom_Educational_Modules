from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=50, verbose_name='название модуля')
    description = models.TextField(verbose_name='описание модуля')