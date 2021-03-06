from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta


@api_view(['POST'])
def createuser(request):
    email = request.data.get('email')
    password = request.data.get('password')
    url = request.data.get("avatar")
    name = request.data.get("name")
    if UserDetails.objects.filter(email=email).exists() and UserDetails.objects.filter(password=password):
        pass
        # print({"Restult": "User Already Exists"})
    else:
        request = {
            'email': email,
            'name': name,
            "password": password,
            "avatar": url
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
    name = request.data.get("name")
    if UserDetails.objects.filter(email=email).exists() and UserDetails.objects.filter(password=password):
        response_data = {
            'token': password,
        }
        return Response(response_data)


@api_view(['GET'])
def getusers(request, pk):
    if pk == 1234567890:
        x = UserDetails.objects.values_list('email', 'name')
        return Response(x)
    else:
        return Response("invalid token")
