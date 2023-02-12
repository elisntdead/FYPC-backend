from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler403, handler404

urlpatterns = [
  path("", views.Home ,name="home"),
  path("contacts/", views.Contacts, name="contacts"),
  path("login/", views.Login, name="login"),
  path("logout/", views.Logout, name="logout"),
  path("join/", views.Join, name="join"),
  path("product/<str:pk>", views.ProductView, name="product"),
  path("product/mark/<str:pk>", views.MarkProduct, name="mark"),
  path("product/add/<str:pk>", views.AddToCart, name="add-cart"),
  path("product/remove/<str:pk>", views.RemoveFromCart, name="remove-cart"),
  path("product/unmark/<str:pk>", views.UnmarkProduct, name="unmark"),
  path("cart/", views.Cart, name="cart"),
  path("cart/confirm/<str:pk>", views.ConfirmOrder, name="confirm"),
  path("myaccount/orders", views.AccountOrders, name="account-orders"),
  path("myaccount/orders/<str:pk>", views.OrderProducts, name="order-products"),
  path("myaccount/favourites", views.AccountFavourites, name="account-favourites"),
  path("myaccount/settings", views.AccountSettings, name="account-settings"),
  path("catalog/", views.Catalog, name="catalog"),
]
handler404 = "base.views.NotFound"
handler403 = "base.views.AccessDenied"