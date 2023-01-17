from django.shortcuts import render, redirect
from Product.models import Product
from Image.models import Image
from User.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Home(request):
  popular = Product.objects.all().order_by('timesBought').filter(deleted__isnull=True)[:2]
  context = {'popular':popular}
  return render(request, "base/index.html", context)

def Contacts(request):
  return render(request, "base/contacts.html")

def Catalog(request):
  products = Product.objects.all().filter(deleted__isnull=True)
  product_filter = ProductFilter(request.GET, queryset=products)
  context = {"product_filter":product_filter}
  return render(request, "base/catalog.html", context)

@login_required(login_url="login")
def Cart(request):
  return render(request, "base/cart.html")

def ProductView(request, pk):
  product = Product.objects.get(id=pk)
  product_images = product.images.all()
  context = {"product":product, "product_images": product_images}
  return render(request, "base/product.html", context)

@login_required(login_url="login")
def AccountOrders(request):
  return render(request, "base/myaccount-orders.html")

@login_required(login_url="login")
def AccountFavourites(request):
  user = request.user
  favourites = user.favourites_set.all()
  context = {"favourites":favourites}
  return render(request, "base/myaccount-favourites.html", context)

@login_required(login_url="login")
def AccountSettings(request):
  return render(request, "base/myaccount-settings.html")

def Login(request):
  if request.user.is_authenticated:
    return redirect("account-orders")

  if request.method == "POST":
    user_login = request.POST.get("login")
    password = request.POST.get("password")
    try:
      user = User.objects.get(Q(email=user_login)|Q(phone=user_login))
    except:
      messages.error(request, "User doesnt exist")

    user = authenticate(request, email=user_login, password=password)

    if user is not None:
      login(request,user)
      return redirect("home")
    else: 
      messages.error(request, "An error occured during authentication")

  return render(request, "base/login.html")


def Join(request):
  return render(request, "base/register.html")