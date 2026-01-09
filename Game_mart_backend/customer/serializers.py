from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer


class RegisterSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
                extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}


        def create(self, validated_data):
                user = User.objects.create_user(
                        username=validated_data["username"],
                        password=validated_data["password"],
                        email=validated_data["email"],
                        first_name=validated_data["first_name"],
                        last_name=validated_data["last_name"]
                        )

                return user
        

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
                extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}


class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Customer
                fields = ['id', 'user', 'address', 'phone_no']
                extra_kwargs = {"id": {"read_only": True}, "user": {"read_only": True}} 