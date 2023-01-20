from django.db import models
from Product.models import Product

# Create your models here.
class Bundle(models.Model):
  product = models.ManyToManyField(Product)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  deleted = models.DateTimeField(null=True, blank=True)