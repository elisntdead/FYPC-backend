from django import forms
from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from User.models import User
""" from django.contrib.auth.models import User """

class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['email', 'password1', 'password2','phone','address']
    widgets = {
      'email':TextInput(attrs={'placeholder':'Enter Your Email'}),
    }
  
  def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder':'Enter Your Password'})
        self.fields['password1'].required=False
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder':'Confirm Password'})
        self.fields['password2'].required=False


class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['email', 'password','phone','address']
    widgets = {
      'email':TextInput(attrs={'placeholder':'Enter Your Email'}),
    }

  def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required=False