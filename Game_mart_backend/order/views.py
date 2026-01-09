from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from customer.models import Customer
from product.models import Product


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def Order_Overview(reuest):
        api_url = {
                'overview': 'order/',
                'checkout': 'order/checkout'
        }

        return Response(api_url, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def CheckOutView(request):
        cart = request.session.get('cart', {})
        customer = Customer.objects.get(user=request.user)
        total_amount = 0
        data = {}

        if customer is not None and len(cart) > 0:
                for product_id, quantity in cart.items():
                        product = Product.objects.get(id=product_id)
                        total_amount += product.price * quantity
                        
                order = Order.objects.create(customer=customer, total_amount=total_amount)
                data['order'] = OrderSerializer(order).data
                data['item'] = []

                for product_id, quantity in cart.items():
                        product = Product.objects.get(id=product_id)
                        subprice = product.price * quantity
                        item = OrderItem.objects.create(order=order, product=product, quantity=quantity, subprice=subprice)
                        serialize_item = OrderItemSerializer(item)
                        data['item'].append(serialize_item.data)
                
                request.session['cart'] = {}
                return Response(data, status=status.HTTP_200_OK)

