import django_filters
from Product.models import Product


class ProductFilter(django_filters.FilterSet):

  class Meta:
    model = Product
    fields = {'price': ['lt', 'gt'], 'name':['icontains']}