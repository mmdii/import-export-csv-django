from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=30)
    lastn = models.CharField(null=True,max_length=30)
    passwd = models.IntegerField(blank=True, null=True)
    