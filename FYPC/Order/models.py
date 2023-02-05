from django.db import models
from User.models import User
from Product.models import Product
from Tag.models import Tag

# Create your models here.


class Order(models.Model):

  STATUSES = [
    (1, 'In Cart'),
    (2, 'Active'),
    (3, 'Finished'),
    (4, 'Waiting for payment'),
    (5, 'Waiting for pickup'),
    (6, 'Cancelled'),
    (7, 'Refund'),
  ]

  client = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
 # worker = models.ForeignKey(Worker, on_delete=models.SET_DEFAULT, null=False, default="deleted")
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  paid = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  delivery = models.BooleanField(null=False, blank=False)
  address = models.CharField(max_length=256, null=True, blank=True)
  status = models.IntegerField(choices=STATUSES, default=1)
  started = models.DateTimeField(null=True, blank=True)
  finished = models.DateTimeField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  cancelled = models.DateTimeField(null=True, blank=True)
  deleted = models.DateTimeField(null=True, blank=True) 
  tags = models.ManyToManyField(Tag, related_name="products")
  
  @property
  def confirm_order(self):
    self.status = 2
    order_products = self.order_products_set.all()
    self.price = 0     
    for order_product in order_products:
      order_product.price = (Product.objects.get(id=order_product.product.id)).price
      order_product.save()
      self.price += order_product.price
      self.save()

  @property
  def cart_price(self):
    price = 0 
    for product in self.order_products_set.all():
      price += product.product.price
    return price



class Order_products(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)