from django.db import models
from Product.models import Product
# Create your models here.
class Promo(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250, null=True, blank=True)
  discounted = models.ManyToManyField(Product, blank=False)
  image = models.ImageField(null=True)
  created = models.DateTimeField(auto_now_add=True)
  deleted = models.DateTimeField(null=True, blank=True)

def __str__(self):
    return self.name
