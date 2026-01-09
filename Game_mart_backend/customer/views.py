from .models import Customer
from .serializers import RegisterSerializer, UserSerializer, CustomerSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, serializers
from rest_framework.response import Response
from django.http import HttpRequest


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def account_overview(request):
        api_urls = {
                "overview": "account/",
                "Register": "account/register",
                "Login": "account/login",
                "refresh": "account/refresh",
                "UserDetails": "account/detail",
                "Update user": "account/update"
        }

        return Response(api_urls, status=status.HTTP_200_OK)


@permission_classes([permissions.AllowAny])
@api_view(['POST'])
def RegisterView(request):
        data = {}
        phone_no = request.data.get("phone_no")
        address = request.data.get("address")
        new_user = RegisterSerializer(data=request.data)

        if User.objects.filter(username=request.data.get("username")).exists():
                raise serializers.ValidationError("This User Already Exist", 400)
        
        new_user.is_valid(raise_exception=True)
        user = new_user.save()

        customer = Customer.objects.create(user=user, address=address, phone_no=phone_no)
        data['user'] = new_user.data
        data['customer'] = CustomerSerializer(customer).data

        return Response(data, status=status.HTTP_201_CREATED)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def CurrentUserDetail(request):
        user = request.user
        print(user)
        print(user.username)

        customer_detail = Customer.objects.get(user=user.id)
        customer_serializer = CustomerSerializer(customer_detail)

        data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'customer': customer_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def Upadte_Customer(request):
        user = request.user
        current_user = User.objects.get(id=user.id)
        customer = Customer.objects.get(user=user.id)

        user_data = {"username": request.data.get("username"),
                     "email": request.data.get("email"),
                     "first_name": request.data.get("first_name"),
                     "last_name": request.data.get("last_name")
                     }
        customer_data = {"address": request.data.get("address"),
                         "phone_no": request.data.get("phone_no")
                        }

        user_serializer = UserSerializer(instance=current_user, data=user_data)
        customer_serializer = CustomerSerializer(instance=customer, data=customer_data)

        if user_serializer.is_valid() and customer_serializer.is_valid():
                user_serializer.save()
                customer_serializer.save()
                data = {"user": user_serializer.data,
                        "customer": customer_serializer.data
                        }
                return Response(data, status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        

# {
# "username": "Derek",
# "email": "bill@gmail.com",
# "password": "1e*289&@?",
# "first_name": "Derek",
# "last_name": "Deepshit",
# "address": "2d 21 road",
# "phone_no": "0392-290290"
# }