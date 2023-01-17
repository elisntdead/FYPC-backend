from django.contrib import admin
from User.models import User
from Product.models import Product, Favourites
from Image.models import Image
from Tag.models import Tag
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Favourites)
admin.site.register(Image)
admin.site.register(Tag)