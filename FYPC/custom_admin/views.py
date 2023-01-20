from django.shortcuts import render, redirect
from User.models import Client, Worker
from Product.models import Product
from bundles.models import Bundle
# Create your views here.
def Admin(request):
  return redirect("clients")

def Clients(request):
  clients = Client.objects.all().order_by("id")
  context = {"clients":clients}
  return render(request, "admin/admin-clients.html", context)

def ClientView(request, pk):
  client = Client.objects.get(id=pk)
  orders = client.order_set.all()
  context = {"client":client, "orders":orders}
  return render(request, "admin/admin-client.html", context)

def Workers(request):
  workers = Worker.objects.all().order_by("id")
  context = {"workers":workers}
  return render(request, "admin/admin-workers.html",context)

def WorkerView(request, pk):
  worker = Worker.objects.get(id=pk)
  orders = worker.order_set.all()
  context = {"worker":worker, "orders":orders}
  return render(request, "admin/admin-worker.html", context)

def Products(request):
  products = Product.objects.all().filter(deleted__isnull=True).order_by("id")
  context = {"products":products}
  return render(request, "admin/admin-products.html",context)

def ProductView(request, pk):
  product = Product.objects.get(id=pk)
  images = product.images.all()
  context = {"product":product, "images":images}
  return render(request, "admin/admin-product.html", context)

def Bundles(request):
  bundles = Bundle.objects.all().filter(deleted__isnull=True).order_by("id")
  context = {"bundles":bundles}
  return render(request, "admin/admin-bundles.html",context)

def BundleView(request, pk):
  bundle = Bundle.objects.get(id=pk)
  products = bundle.product.all()
  context = {"bundle":bundle, "products":products}
  return render(request, "admin/admin-bundle.html", context)