from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
from .serializer import LoginSerializer, RegisterUserSerializer
from .models import User
from django.http import HttpRequest
from django.contrib.auth import login, logout
from rest_framework.authtoken.views import APIView
from django.views import View
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
import re
from django.utils.crypto import get_random_string

def check_email(email):
    user = User.objects.filter(email=email, is_active=True).first()
    if user is None:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, email)):
            return True
    return False


def check_user(username):
    user = User.objects.filter(username=username).first()
    if user is not None:
        return False
    return True


def check_password(password):
    return True


class CreateUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request: HttpRequest):
        return Response({'parametrs': {'username': 'charfield-uniqe', 'password': 'charfield', 'fname': 'charfield',
                                       'lname': 'charfield', 'email': '.@gmail.com'}, 'detail': 'register user'})

    def post(self,request:HttpRequest):
        register_user = RegisterUserSerializer(data=request.data)
        print(register_user)
        if register_user.is_valid():
            if check_user(register_user.data['username']):
                if check_email(register_user.data['email']):
                    if check_password(register_user.data['password']):
                        user_created=User.objects.create(username=register_user.data['username'],fname=register_user.data['fname'],lname=register_user.data['lname'],email=register_user.data['email'])
                        user_created.set_password(register_user.data['password'])
                        user_created.code=get_random_string(100)
                        user_created.save()
                        #send email
                        return Response(
                            {'activate account': 'false', 'status': status.HTTP_200_OK,
                             'detail': 'Your account has been created and the activation code has been sent to your email'})
                    else:
                        return Response({'status': status.HTTP_400_BAD_REQUEST,
                                         'detail': 'your passwrod is easy'})
                else:
                    return Response({'status': status.HTTP_400_BAD_REQUEST,
                                     'detail': 'Your email is incorrect or already exists'})
            else:
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                                 'detail': 'username is invalid'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'detail': 'invalid fields'})



class LoginUser(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request: HttpRequest):
        return Response({'parametrs': {'username': 'charfield', 'password': 'charfield'}, 'detail': 'loginform'})

    def post(self, request: HttpRequest):
        loginform = LoginSerializer(data=request.data)
        if loginform.is_valid():
            user = User.objects.filter(username=loginform.data['username']).first()
            if user is not None:
                print(user.username)
                password = loginform.data['password']
                if user.check_password(password):
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key, 'status': status.HTTP_200_OK, 'detail': 'You are logged in'})
                else:
                    return Response({'status': status.HTTP_204_NO_CONTENT,
                                     'detail': 'Incorrect password'})

            else:
                return Response({'status': status.HTTP_204_NO_CONTENT,
                                 'detail': 'Incorrect username'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': 'Incorrect information'})

@api_view(['GET'])
def ActiveAccount(request,code):
    user=User.objects.filter(code=code , is_active=False).first()
    if user is not None:
        user.is_active=True
        user.code=get_random_string(100)
        user.save()
        return Response({'status':status.HTTP_200_OK,'detail':'your account is activated'})
    else:
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': 'invalid active code '})




{
    "email": "",
    "token": "1232d49ec34472f1d6e8a5bf1afaf2036777d04a",
    "user_id": 1
}

