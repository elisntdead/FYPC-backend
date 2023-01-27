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
    path("products/create/", views.ProductAdd, name="add-product"),
    path("products/edit/<str:pk>", views.ProductEdit, name="edit-product"),
    path("products/delete/<str:pk>", views.ProductDelete, name="delete-product"),
    path("bundles/", views.Bundles, name="bundles"),
    path("bundles/<str:pk>", views.BundleView, name="view-bundle"),
    path("reviews/", views.Reviews, name="reviews"),
    path("reviews/<str:pk>", views.ReviewView, name="view-review"),
    path("reviews/edit/<str:pk>", views.ReviewEdit, name="edit-review"),
    path("reviews/delete/<str:pk>", views.ReviewDelete, name="delete-review"),
]