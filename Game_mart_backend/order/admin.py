from django.contrib import admin
from .models import Order, OrderItem, OrderStatus


class OrderAdmin(admin.ModelAdmin):
        model = Order
        fields = ['id', 'customer', 'total_amount', 'status', 'order_date']
        readonly_fields = ['id', 'order_date']
        list_display = ['id', 'customer', 'total_amount', 'status', 'order_date']
        list_filter = ['customer', 'status']
        actions = ["update_status"]

def update_status(model_admin, request, queryset):
        queryset.update(
                status = OrderStatus.DELIVERED
        )


class OrderItemAdmin(admin.ModelAdmin):
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'subprice']
        readonly_fields = ['id']
        list_display = ['id', 'order', 'product', 'quantity', 'subprice']
        list_filter = ['order', 'product']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)