from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home ,name="home"),
  path("contacts/", views.Contacts, name="contacts"),
  path("login/", views.Login, name="login"),
  path("logout/", views.Logout, name="logout"),
  path("join/", views.Join, name="join"),
  path("product/<str:pk>", views.ProductView, name="product"),
  path("product/mark/<str:pk>", views.MarkProduct, name="mark"),
  path("product/unmark/<str:pk>", views.UnmarkProduct, name="unmark"),
  path("cart/", views.Cart, name="cart"),
  path("myaccount/orders", views.AccountOrders, name="account-orders"),
  path("myaccount/favourites", views.AccountFavourites, name="account-favourites"),
  path("myaccount/settings", views.AccountSettings, name="account-settings"),
  path("catalog/", views.Catalog, name="catalog"),
]
