from django.urls import path
from . import views


urlpatterns = [
        path("cart/", views.Cart_Overview, name="overview"),
        path("cart/add", views.AddToCart, name="add_to_cart"),
        path("cart/all", views.GetCart, name="get_cart"),
        path("cart/decrease", views.DecreaseFromCart, name="decrease_cart"),
        path("cart/remove", views.RemoveFromCart, name="remove_cart"),
        path("cart/clear", views.ClearCart, name="clear_cart"),
]