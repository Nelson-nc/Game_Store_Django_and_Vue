from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
        class Meta:
                model = Order
                fields = ['id', 'customer', 'total_amount', 'status']
                extra_kwargs = {"id": {"read_only": True}}


class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
                model = OrderItem
                fields = ['id', 'order', 'product', 'quantity', 'subprice']
                extra_kwargs = {"id": {"read_only": True}}