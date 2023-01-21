from django.db import models
from User.models import Client, Worker, User
from Product.models import Product

# Create your models here.


class Order(models.Model):

  STATUSES = [
    (1, 'In Cart'),
    (2, 'Active'),
    (3, 'Finished'),
    (4, 'Waiting for pay'),
    (5, 'Waiting for pickup')
  ]

  client = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
 # worker = models.ForeignKey(Worker, on_delete=models.SET_DEFAULT, null=False, default="deleted")
  price = models.DecimalField(max_digits=7, decimal_places=2)
  paid = models.DecimalField(max_digits=7, decimal_places=2)
  delivery = models.BooleanField()
  address = models.CharField(max_length=256)
  status = models.IntegerField(choices=STATUSES, default=0)
  started = models.DateTimeField()
  finished = models.DateTimeField()
  created = models.DateTimeField(auto_now_add=True)
  cancelled = models.DateTimeField(null=True, blank=True)
  deleted = models.DateTimeField(null=True, blank=True)


class Order_products(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)