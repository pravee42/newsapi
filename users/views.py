from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta


def createuser(email, password, avatar, name):
    request = {
        'email' : email,
        'name' : name,
        "password" : password,
        "avatar" : avatar
    }
    serializer = UserDetailserializers(data=request)
    if serializer.is_valid():
        serializer.save()
    else:
        print(request.data)
    return Response(serializer.data)

@api_view(['POST'])
def loginuser(request):
    email = request.data.get('email')
    password = request.data.get('password')
    url = request.data.get("avatar")
    name = request.data.get("name")
    if UserDetails.objects.filter(email=email).exists() and UserDetails.objects.filter(password=password):
        response_data = {
            'token': password,
            'avatar': url
        }
        return Response(response_data)
    else:
        createuser(email, password, url, name)


@api_view(['GET'])
def getusers(request, pk):
    if pk == 1234567890:
        x = UserDetails.objects.values_list('email', 'name')
        return Response(x)
    else:
        return Response("invalid token")