from rest_framework import serializers
from .models import SharedNews


class SharedNewsserializer(serializers.ModelSerializer):
    class Meta:
        model = SharedNews
        fields = '__all__'


