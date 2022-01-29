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
        authordata = AuthorArticles.objects.all()
        authordataserializer = AuthorArticlesSerializer(authordata, many=True)
        data = {
            'atricles': serializer.data,
            'author': authordataserializer.data
        }
        return Response(data)

    def post(self, request, format=None):
        email = request.data.get('email')
        data = {
            "author": request.data.get('author'),
            "published_date": request.data.get('published_date'),
            "votes": request.data.get('votes'),
            "title": request.data.get('title'),
            "article": request.data.get('article')
        }
        print(data)
        serializer = ArticlesSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            saveAuthor(serializer.data.get('id'), email)
            # print(serializer.data, "serializer data")
            # print(serializer.data.get('id'), "serializer id")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticlesDetail(APIView):

    def get_object(self, pk):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticlesSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticlesSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentsClass(APIView):
    def get(self, request, format=None):
        snippets = Comments.objects.all()
        serializer = CommentsSerializer(snippets, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetail(APIView):

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def saveAuthor(articleid, email):
    data = {'creator_email': email, 'articleid': articleid}
    serializer = AuthorArticlesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return data
