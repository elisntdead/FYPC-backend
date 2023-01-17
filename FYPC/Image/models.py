from django.db import models
from Product.models import Product

# Create your models here.
class Image(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')
  image = models.ImageField(null=True, default="placeholder_product.jpg")
  is_first = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  deleted = models.DateTimeField(null=True, blank=True)

  class Meta:
    ordering = ['-is_first', 'created']