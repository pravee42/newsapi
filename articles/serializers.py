from rest_framework import serializers
from .models import Articles, Comments, Authorarticles


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class AuthorArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorarticles
        fields = '__all__'
