from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta


def createuser(email, name, password, avatar):
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
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def loginuser(request):
    email = request.data.get('email')
    password = request.data.get('password')
    url = request.data.get("avatar")
    name = request.data.get("name")
    if UserField.objects.filter(username=username).exists() and UserField.objects.filter(password=password):
        response_data = {
            'token': password
        }
        return Response(response_data)
    else:
        createuser(email, password, url, name)