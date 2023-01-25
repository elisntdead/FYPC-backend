from django.forms import ModelForm, TextInput, NumberInput, Textarea
from Product.models import Product

#forms

class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    exclude = ['created', 'deleted','timesBought', 'tags']
    widgets = {
      'name':TextInput(attrs={'class':'form-control'}),
      'price':NumberInput(attrs={'class':'form-control'}),
      'description':Textarea(attrs={'class':'form-control'}),
      'installTime':NumberInput(attrs={'class':'form-control'}),
    }