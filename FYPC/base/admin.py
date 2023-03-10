from django.contrib import admin
from User.models import User
from Product.models import Product, Favourites
from Image.models import Image
from Tag.models import Tag
from Order.models import Order, Order_products
from bundles.models import Bundle
from Review.models import Review
from Promo.models import Promo
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Favourites)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Bundle)
admin.site.register(Promo)
admin.site.register(Order_products)
