from django.db import models

# Create your models here.
class Order(models.Model):
     address = models.CharField(max_length=180, null=True, blank=True)
     meal = models.CharField(max_length=180, null=True, blank=True)

# Create your models here.
