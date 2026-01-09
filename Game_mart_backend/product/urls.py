from django.urls import path
from . import views


urlpatterns = [
        path("product/", views.product_overview, name="product_overview"),
        path("product/all", views.ProductView, name="product_view"),
        path("product/platforms/", views.PlatformView, name="platform_view"),
        path("product/genres/", views.GenreView, name="genre_view"),
        path("product/detail/<int:pk>", views.GetProductView, name="get_product"),
]