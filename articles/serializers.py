from rest_framework import serializers
from .models import Articles, Comments


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
