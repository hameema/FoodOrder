from django.db import models

# Create your models here.
class student (models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=225)

class menu (models.Model):
    dish = models.CharField(max_length=225)
    prise = models.IntegerField()

class order (models.Model):
    dish = models.CharField(max_length=225)
    note = models.TextField()
