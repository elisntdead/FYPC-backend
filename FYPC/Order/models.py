from django.db import models
from User.models import Client, Worker, User

# Create your models here.
class Order(models.Model):
  client = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
 # worker = models.ForeignKey(Worker, on_delete=models.SET_DEFAULT, null=False, default="deleted")
  price = models.DecimalField(max_digits=7, decimal_places=2)
  paid = models.DecimalField(max_digits=7, decimal_places=2)
  delivery = models.BooleanField()
  address = models.CharField(max_length=256)
  #status = 
  started = models.DateTimeField()
  finished = models.DateTimeField()
  created = models.DateTimeField(auto_now_add=True)
  cancelled = models.DateTimeField(null=True, blank=True)
  deleted = models.DateTimeField(null=True, blank=True)