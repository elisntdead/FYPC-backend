from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Admin),
    path("clients/", views.Clients, name="clients"),
    path("clients/<str:pk>", views.ClientView, name="view-client"),
    path("workers/", views.Workers, name="workers"),
    path("workers/<str:pk>", views.WorkerView, name="view-worker"),
    path("products/", views.Products, name="products"),
    path("products/<str:pk>", views.ProductView, name="view-product"),
    path("bundles/", views.Bundles, name="bundles"),
    path("bundles/<str:pk>", views.BundleView, name="view-bundle"),
]