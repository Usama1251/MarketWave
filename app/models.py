from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

  
