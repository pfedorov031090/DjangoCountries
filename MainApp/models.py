from django.db import models

# Create your models here.


class Languages(models.Model):
    language = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Languages)
