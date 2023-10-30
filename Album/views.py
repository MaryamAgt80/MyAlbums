from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
from .serializer import AlbumSerializer
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


class CreateAlbum(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: HttpRequest):
        return Response({'parametrs': {'name': 'name_album', 'is_public': '0/1(pravite/public)'},
                         'detail': 'create album (user authenicated)'})

    def post(self, request: HttpRequest):
        data = request.data
        user = User.objects.filter(id=request.user.id).first()
        data['user'] = user.pk
        Album_create = AlbumSerializer(data=data)
        if Album_create.is_valid():
            Album_create.save()
            return Response({'status': status.HTTP_201_CREATED, 'detail': 'Album Created'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': 'Incorrect information'})
