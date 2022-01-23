from .models import * 
from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ArticlesClass(APIView):
    def get(self, request, format=None):
        snippets = Articles.objects.all()
        serializer = ArticlesSerializers(snippets, many=True)

        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)