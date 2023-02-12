from django.shortcuts import render, redirect
from User.models import User
from Product.models import Product
from Image.models import Image
from bundles.models import Bundle
from Tag.models import Tag
from Review.models import Review
from django.utils import timezone
from .forms import ProductForm, ReviewForm, RoleForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@staff_member_required(login_url="login")
def Admin(request):
  return redirect("clients")

@staff_member_required(login_url="login")
def Clients(request):
  clients = User.objects.filter(is_active=True, is_staff=False).order_by("id")
  context = {"clients":clients}
  return render(request, "admin/admin-clients.html", context)

@staff_member_required(login_url="login")
def ClientView(request, pk):
  client = User.objects.get(id=pk)
  orders = client.order_set.exclude(status = 1)
  context = {"client":client, "orders":orders}
  return render(request, "admin/admin-client.html", context)

@staff_member_required(login_url="login")
def Workers(request):
  workers = User.objects.filter(is_active=True, is_staff=True).order_by('id')
  context = {"workers":workers}
  return render(request, "admin/admin-workers.html",context)

@staff_member_required(login_url="login")
def WorkerView(request, pk):
  worker = User.objects.get(id=pk)
  orders = worker.order_set.all()
  context = {"worker":worker, "orders":orders}
  return render(request, "admin/admin-worker.html", context)

@staff_member_required(login_url="login")
def Products(request):
  products = Product.objects.all().filter(deleted__isnull=True).order_by("id")
  context = {"products":products}
  return render(request, "admin/admin-products.html",context)

@staff_member_required(login_url="login")
def ProductView(request, pk):
  product = Product.objects.get(id=pk)
  images = product.images.all()
  tags = product.tags.all()
  context = {"product":product, "images":images, "tags":tags}
  return render(request, "admin/admin-product.html", context)

@staff_member_required(login_url="login")
def ProductAdd(request):
  form = ProductForm()
  page = "add"
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      product = form.save()
      return redirect("products")
  context = {"form":form, "page":page}
  return render(request, "admin/admin-product-edit.html", context)

@staff_member_required(login_url="login")
def ProductEdit(request, pk):
  page = "edit"
  product = Product.objects.get(id=pk)
  tags = product.tags.all()
  form = ProductForm(instance=product)
  if request.method == "POST":
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      product = form.save()
      return redirect("view-product", product.id)
  context = {"page":page, "form":form, "product":product, "tags":tags}
  return render(request, "admin/admin-product-edit.html", context)

@staff_member_required(login_url="login")
def ProductDelete(request, pk):
  product = Product.objects.get(id=pk)
  product.deleted = timezone.now()
  product.save()
  return redirect("products")

@staff_member_required(login_url="login")
def Bundles(request):
  bundles = Bundle.objects.all().filter(deleted__isnull=True).order_by("id")
  context = {"bundles":bundles}
  return render(request, "admin/admin-bundles.html",context)

@staff_member_required(login_url="login")
def BundleView(request, pk):
  bundle = Bundle.objects.get(id=pk)
  products = bundle.product.all()
  context = {"bundle":bundle, "products":products}
  return render(request, "admin/admin-bundle.html", context)


@staff_member_required(login_url="login")
def Reviews(request):
  reviews = Review.objects.filter(deleted__isnull=True).order_by("id")
  context = {"reviews":reviews}
  return render(request, "admin/admin-reviews.html",context)

@staff_member_required(login_url="login")
def ReviewView(request, pk):
  review = Review.objects.get(id=pk)
  context = {"review":review}
  return render(request, "admin/admin-review.html", context)

@staff_member_required(login_url="login")
def ReviewEdit(request, pk):
  page = "edit"
  review = Review.objects.get(id=pk)
  form = ReviewForm(instance=review)
  if request.method == "POST":
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
      review = form.save(commit=False)
      if review.approved is None:
        review.approved = timezone.now()
      form.save()
      return redirect("view-review", review.id)
  context = {"page":page, "form":form, "review":review}
  return render(request, "admin/admin-review-edit.html", context)

@staff_member_required(login_url="login")
def ReviewDelete(request, pk):
  review = Review.objects.get(id=pk)
  review.deleted = timezone.now()
  review.save()
  return redirect("reviews")

@staff_member_required(login_url="login")
def Roles(request):
  roles = Group.objects.all()
  context = {"roles":roles}
  return render(request, "admin/admin-roles.html",context)

@staff_member_required(login_url="login")
def RoleView(request, pk):
  role = Group.objects.get(id=pk)
  role_permissions = role.permissions.all()
  context = {"role":role, "role_permissions":role_permissions}
  return render(request, "admin/admin-role.html", context)

@staff_member_required(login_url="login")
def RoleAdd(request):
  form = RoleForm()
  page = "add"
  if request.method == "POST":
    form = RoleForm(request.POST)
    if form.is_valid():
      role = form.save()
      return redirect("roles")
  context = {"form":form, "page":page}
  return render(request, "admin/admin-role-edit.html", context)

@staff_member_required(login_url="login")
def RoleEdit(request, pk):
  page = "edit"
  role = Group.objects.get(id=pk)
  role_permissions = role.permissions.all()
  form = RoleForm(instance=role)
  if request.method == "POST":
    form = RoleForm(request.POST, instance=role)
    if form.is_valid():
      role = form.save()
      return redirect("view-role", role.id)
  context = {"page":page, "form":form, "role":role, "role_permissions":role_permissions}
  return render(request, "admin/admin-role-edit.html", context)

@staff_member_required(login_url="login")
def RoleDelete(request, pk):
  role = Group.objects.get(id=pk)
  role.delete()
  return redirect("roles")

@staff_member_required(login_url="login")
def RoleAddPermission(request, pk):
  role = Group.objects.get(id=pk)
  add_permissions = Permission.objects.exclude(group__name=role.name).order_by("id")
  context = {"role":role, "add_permissions":add_permissions}
  return render(request, "admin/admin-add-permission.html", context)

@staff_member_required(login_url="login")
def AddPermission(request, pk, permission_id):
  role = Group.objects.get(id=pk)
  permission = Permission.objects.get(id=permission_id)
  role.permissions.add(permission)
  return redirect("edit-role", role.id)

@staff_member_required(login_url="login")
def RemovePermission(request, pk, permission_id):
  role = Group.objects.get(id=pk)
  permission = Permission.objects.get(id=permission_id)
  role.permissions.remove(permission)
  return redirect("edit-role", role.id)

@staff_member_required(login_url="login")
def Tags(request):
  tags = Tag.objects.all().order_by("id")
  context = {"tags":tags}
  return render(request, "admin/admin-tags.html" ,context)