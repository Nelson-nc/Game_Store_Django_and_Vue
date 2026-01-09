from django.db import models
from django.http import HttpRequest


class Platform(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self) -> str:
                return self.name


class Genre(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self) -> str:
                return self.name


class Product(models.Model):
        name = models.CharField(max_length=200)
        image = models.ImageField(upload_to="product_image")
        price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        company = models.CharField(max_length=100)
        genre = models.ManyToManyField(Genre, related_name="product")
        platform = models.ManyToManyField(Platform, related_name="product")

        def __str__(self) -> str:
                return f"{self.name}"