from django.shortcuts import render
from users.models import *
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta

@api_view(['POST'])
def bookmark(request):
    email = request.data.get('email')
    news = request.data.get('password')
    source = request.data.get("avatar")
    image = request.data.get("name")
    if UserDetails.objects.filter(email=email).exists():
        data1 = {
            "email" : email,
            "news" : news,
            "source" : source,
            "image" : image
        }
        serializer = Bookmarkserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data1)
        else:
            print(serializer)
    else:
        print("Error Creating bookmarkS")
    return Response("")