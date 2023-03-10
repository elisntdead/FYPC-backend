from django.db import models
from User.models import User
from Tag.models import Tag
# Create your models here.



class Product(models.Model): 
  CATEGORIES = [
    (1, 'PC'),
    (2, 'Laptop'),
    (3, 'Maintenance'),
    (4, 'Accessory'),
    (5, 'Software'),
    (6, 'Miscellaneous')
  ]

  name = models.CharField(max_length=60)
  description = models.TextField()
  category = models.IntegerField(choices=CATEGORIES, default=1)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  installTime = models.IntegerField(null=True, blank=True)
  timesBought = models.IntegerField(default=0)
  tags = models.ManyToManyField(Tag, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  deleted = models.DateTimeField(null=True, blank=True)

  
  def __str__(self):
    return self.name[0:40]


  def get_first_image(self):
    try:
      first_image = self.images.first().image
      return first_image
    except AttributeError:
      return

  def short_description(self):
    short_desc = self.description[:256]
    if len(self.description) > 256:
      short_desc += "..."
    return short_desc

class Favourites(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)