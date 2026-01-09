from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Platform, Product, Genre
from .serializers import ProductSerializer, PlatformSerializer, GerneSerializer


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def product_overview(request):
        api_urls = {
                "product overview": "product/",
                "all product": "product/all/",
                "all platforms": "product/platforms/",
                "all genres": "product/genres/",
                "search by name": "product/all?name__icontains=name",
                "search by genre": "product/all?genre=genre_name",
                "search by platform": "product/all?platform=platform_name",
                "get product": "product/detail/<int:pk>"
        }

        return Response(api_urls, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def ProductView(request):
        if request.query_params:
                products = Product.objects.filter(**request.query_params.dict())
        else:
                products = Product.objects.order_by('?').all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def PlatformView(request):
        platforms = Platform.objects.order_by('?').all()
        serializer = PlatformSerializer(platforms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def GenreView(request):
        genres = Genre.objects.order_by('?').all()
        serializer = GerneSerializer(genres, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def GetProductView(request, pk):
        product = Product.objects.get(pk=pk)
        if product:
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
                return Response("product not found", status=status.HTTP_404_NOT_FOUND)
