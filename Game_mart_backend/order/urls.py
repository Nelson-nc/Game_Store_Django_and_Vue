from django.urls import path
from . import views


urlpatterns = [
        path("order/", views.Order_Overview, name="order_overview"),
        path("order/checkout", views.CheckOutView, name="order_checkout"),
]