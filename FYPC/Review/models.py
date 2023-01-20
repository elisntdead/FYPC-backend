from django.db import models
from User.models import User
from Product.models import Product
# Create your models here.
class Review(models.Model):
  client = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  text = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  deleted = models.DateTimeField(null=True, blank=True)
  approved = models.DateTimeField()