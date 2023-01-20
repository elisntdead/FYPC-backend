from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from User.models import Client #подключаем модель которую мы будем обрабатывать формой
""" from django.contrib.auth.models import User """

class UserForm(ModelForm):
  class Meta:
    model = User # модель на которую влияет форма
    fields = ['email'] #так можно заполнять нужные поля для формы