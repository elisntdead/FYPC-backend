from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length=50, null=True, blank=True)
  email = models.EmailField(unique=True, null=True)
  phone = PhoneNumberField(null=True, blank=True)


  USERNAME_FIELD = "email"
  REQUIRED_FIELDS =[]


class Client(User):
  address = models.CharField(max_length=100, null=True, blank=True)


class Worker(User):
  pass