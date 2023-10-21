from rest_framework import serializers
from . models import User
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=200)

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['fname','lname','username','email','password']