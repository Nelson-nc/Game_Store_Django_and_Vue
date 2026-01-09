from django.contrib import admin
from .models import Product, Platform, Genre


class ProductAdmin(admin.ModelAdmin):
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at', 'genre', 'platform', 'image']
        readonly_fields = ['id', 'created_at']
        list_display = ['id', 'name', 'price', 'created_at']
        list_filter = ['price', 'created_at']
        search_fields = ['name']


class PlatformAdmin(admin.ModelAdmin):
        model = Platform
        fields = ['id', 'name']
        readonly_fields = ['id']
        list_display = ['id', 'name']
        search_fields = ['name']


class GenreAdmin(admin.ModelAdmin):
        model = Genre
        fields = ['id', 'name']
        readonly_fields = ['id']
        list_display = ['id', 'name']
        search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)