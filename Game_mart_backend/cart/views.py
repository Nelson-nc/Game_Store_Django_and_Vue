from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from product.models import Product
from product.serializers import ProductSerializer


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def Cart_Overview(request):
        api_urls = {
                "overview": "cart/",
                "add to cart": "cart/add",
                "all in cart": "cart/all",
                "decreaseitem in cart": "cart/decrease",
                "remove from cart": "cart/remove",
                "clear cart": "cart/clear",
        }

        return Response(api_urls, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def AddToCart(request):
        product_id = str(request.data.get("product"))
        cart = request.session.get('cart', {})

        if product_id in cart:
                cart[product_id] += 1
                request.session['cart'] = cart
        else:
                cart[product_id] = 1
                request.session['cart'] = cart

        return Response(cart.items(), status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def GetCart(request):
        cart = request.session.get('cart', {})
        data = []

        if len(cart) > 0:
                for product_id, quantity in cart.items():
                        product = Product.objects.get(id=product_id)
                        product_data = ProductSerializer(product)
                        data.append({"product":product_data.data, "quantity":quantity})

                return Response(data, status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def DecreaseFromCart(request):
        product_id = str(request.data.get("product"))
        cart = request.session.get('cart', {})

        if product_id in cart:
                if cart[product_id] > 1:
                        cart[product_id] -= 1
                        request.session['cart'] = cart
                else:
                        cart[product_id] = 1
                        request.session['cart'] = cart

                return Response(cart.items(), status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def RemoveFromCart(request):
        product_id = str(request.data.get("product"))
        cart = request.session.get('cart', {})

        if product_id in cart:
                cart.pop(product_id, None)
                request.session['cart'] = cart
                return Response(cart.items(), status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def ClearCart(request):
        request.session['cart'] = {}
        return Response(status=status.HTTP_204_NO_CONTENT)