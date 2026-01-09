from rest_framework import serializers
from .models import Product, Platform, Genre


class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = ['id', 'name', 'price', 'description', 'created_at', 'genre', 'platform', 'image']
                extra_kwargs = {"id": {"read_only": True}}


class PlatformSerializer(serializers.ModelSerializer):
        class Meta:
                model = Platform
                fields = ['id', 'name']
                extra_kwargs = {"id": {"read_only": True}}


class GerneSerializer(serializers.ModelSerializer):
        class Meta:
                model = Genre
                fields = ['id', 'name']
                extra_kwargs = {"id": {"read_only": True}}
