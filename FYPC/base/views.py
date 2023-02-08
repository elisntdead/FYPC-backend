from django.shortcuts import render, redirect, HttpResponseRedirect
from Product.models import Product, Favourites
from Image.models import Image
from User.models import User
from Promo.models import Promo
from Order.models import Order, Order_products
from django.db.models import Q, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .forms import UserForm
from django.core.exceptions import PermissionDenied
from django.http import Http404

# Create your views here.

def CartCheckCreate(user):
  if Order.objects.filter(client=user, status=1).exists():
    order = Order.objects.get(client=user, status=1)
  else:
    order = Order.objects.create(
      client = user,
      status = 1,
      delivery = False,
      paid = 0,
      price = 0
    )
  return order

def Home(request):
  products = Product.objects.all().filter(deleted__isnull=True)
  popular = products.order_by('-timesBought')[:10]
  promos = Promo.objects.all().filter(deleted__isnull=True)
  pcs = products.order_by('?').filter(category=1)[:6]
  laptops = products.order_by('?').filter(category=2)
  maintenance = products.order_by('?').filter(category=3)
  accessories = products.order_by('?').filter(category=4)
  software = products.order_by('?').filter(category=5)
  context = {'popular':popular, "promos":promos, "pcs":pcs, "laptops":laptops, "maintenance":maintenance, "accessories":accessories, "software":software}
  return render(request, "base/index.html", context)

def Contacts(request):
  return render(request, "base/contacts.html")

def Catalog(request):
  products = Product.objects.all().filter(deleted__isnull=True)
  product_filter = ProductFilter(request.GET, queryset=products)
  paginated_products = Paginator(product_filter.qs, 4)
  page_number = request.GET.get("page")
  page_obj = paginated_products.get_page(page_number)
  context = {"product_filter":product_filter, "page_obj":page_obj}
  return render(request, "base/catalog.html", context)

@login_required(login_url="login")
def Cart(request):
  user = request.user
  order = CartCheckCreate(user)
  products = order.order_products_set.all()
  context = {"order":order, "products":products, "price":order.cart_price}
  return render(request, "base/cart.html", context)

@login_required(login_url="login")
def ConfirmOrder(request, pk):
  order = Order.objects.get(id=pk, status=1)
  if order.order_products_set.exists():
    if request.user == order.client:
      order.confirm_order
    else: 
      raise PermissionDenied()
    return redirect("account-orders")
  else:
    messages.error(request, "You haven't added any products to your cart")
    return redirect("cart")

@login_required(login_url="login")
def AddToCart(request, pk):
  user = request.user
  add_product = Product.objects.get(id=pk)
  cart_order = CartCheckCreate(user)
  product = Order_products.objects.create(
  order = cart_order,
  product = add_product
  )
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="login")
def RemoveFromCart(request, pk):
  cart_order = Order.objects.get(client = request.user, status=1)
  try:
    added = Order_products.objects.filter(order = cart_order, product=pk).first()
    added.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  except:
    return redirect("home")

def ProductView(request, pk):
  product = Product.objects.get(id=pk)
  product_images = product.images.all()
  similar_products = Product.objects.filter(tags__in=product.tags.all()).exclude(pk=product.pk).distinct().annotate(num_matching_tags=Count('tags', filter=Q(tags__in=product.tags.all())))
  similar_products = similar_products.order_by('-num_matching_tags')[:6]
  context = {"product":product, "product_images": product_images, "similar_products":similar_products}
  return render(request, "base/product.html", context)

@login_required(login_url="login")
def MarkProduct(request, pk):
  mark_product = Product.objects.get(id=pk)
  product_is_marked = Favourites.objects.filter(user=request.user, product=mark_product).exists()
  if product_is_marked:
    return redirect("home")
  else:
    marked = Favourites.objects.create(
    user = request.user,
    product = mark_product
   )
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  
@login_required(login_url="login")
def UnmarkProduct(request, pk):
  marked = Favourites.objects.get(product=pk, user = request.user)
  marked.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="login")
def AccountOrders(request):
  page = "orders"
  client = User.objects.get(id=request.user.id)
  orders = client.order_set.exclude(Q(status=1) | Q(deleted__isnull=False))
  context = {"client":client, "orders":orders, "page":page}
  return render(request, "base/myaccount-orders.html",context)

@login_required(login_url="login")
def OrderProducts(request, pk):
  order = Order.objects.get(id=pk)
  if (request.user != order.client) | (order.status == 1):
    raise PermissionDenied()
  products = order.order_products_set.all()
  context = {"order":order, "products":products}
  return render(request, "base/show-order-products.html" ,context)

@login_required(login_url="login")
def AccountFavourites(request):
  page = "favourites"
  user = request.user
  favourites = user.favourites_set.all()
  context = {"favourites":favourites, "page":page}
  return render(request, "base/myaccount-favourites.html", context)

@login_required(login_url="login")
def AccountSettings(request):
  page = "settings"
  user = request.user
  form = UserForm(instance=user)
  if request.method == "POST":
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      login(request, user)
  context = {"form":form, "page":page}
  return render(request, "base/myaccount-settings.html", context)

def Login(request):
  if request.user.is_authenticated:
    return redirect("account-orders")

  if request.method == "POST":
    user_login = request.POST.get("login")
    password = request.POST.get("password")
    try:
      user = User.objects.get(Q(email=user_login))
    except:
      messages.error(request, "User doesnt exist")

    user = authenticate(request, email=user_login, password=password)

    if user is not None:
      login(request,user)
      return redirect("home")
    else: 
      messages.error(request, "An error occured during authentication")
  return render(request, "base/login.html")

def Logout(request):
    logout(request)
    return redirect('home')

def Join(request):
  form = UserForm()
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("home")
    else:
      messages.error(request, "There's an error during registration")
  context = {"form":form}
  return render(request, "base/register.html", context)

def NotFound(request, exception=None):
  return render(request, "404.html", status=404)

def AccessDenied(request, exception=None):
  return render(request, "403.html", status=403)