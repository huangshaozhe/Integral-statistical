from django.db import models

# Create your models here.

class integral(models.Model):
    name = models.CharField(max_length=32)
    integral = models.CharField(max_length=128)
