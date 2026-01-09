from django.db import models
from customer.models import Customer
from product.models import Product


class OrderStatus(models.TextChoices):
        PENDING = 'Pending', "pending"
        DELIVERED = 'Delivered', 'delivered'


class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        order_date = models.DateTimeField(auto_now_add=True)
        total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
        status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING)

        def __str__(self) -> str:
                return f"ID:{self.pk} <==> USER:{self.customer.user.username}"


class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        subprice = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

        def __str__(self) -> str:
                return f"Order_ID: {self.order.pk}"