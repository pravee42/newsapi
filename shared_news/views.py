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
def add_news_to_db(request):
    news = request.data.get('news')
    source = request.data.get("link")
    image = request.data.get("image")

    data1 = {
        "news": news,
        "source": source,
        "image": image
    }
    print(data1)
    serializer = SharedNewsserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data1)
    else:
        print(serializer)

    return Response("News Sharing link created successfully")


@api_view(['GET'])
def getsharedNews(request, pk):
    data = SharedNews.objects.filter(id=pk)
    serializer = SharedNewsserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
