import django_filters
from django_filters import ChoiceFilter
from django import forms
from Product.models import Product


class ProductFilter(django_filters.FilterSet):

  price__lt = django_filters.NumberFilter(field_name='price',  lookup_expr='lt', widget = forms.NumberInput(attrs={'placeholder':'Price Less Than'}))
  price__gt = django_filters.NumberFilter(field_name='price',  lookup_expr='gt', widget = forms.NumberInput(attrs={'placeholder':'Price Higher Than'}))
  name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', widget = forms.TextInput(attrs={'placeholder':'Name Contains'}))
  category = django_filters.ChoiceFilter(choices=Product.CATEGORIES)