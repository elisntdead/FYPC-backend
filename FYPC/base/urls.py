from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home ,name="home"),
  path("contacts/", views.Contacts, name="contacts"),
  path("login/", views.Login, name="login"),
  path("join/", views.Join, name="join"),
  path("product/<str:pk>", views.ProductView, name="product"),
  path("cart/", views.Cart, name="cart"),
  path("myaccount/orders", views.AccountOrders, name="account-orders"),
  path("myaccount/favourites", views.AccountFavourites, name="account-favourites"),
  path("myaccount/settings", views.AccountSettings, name="account-settings"),
  path("catalog/", views.Catalog, name="catalog"),
]
