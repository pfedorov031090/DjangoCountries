from django.db import models

# Create your models here.

# FIXME: классы никогда не называются во множественном числе
#   Languages --> Language
class Languages(models.Model):
    # FIXME: крайне неудачное название поля. У языка есть язык?
    language = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Languages)
