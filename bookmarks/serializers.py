from rest_framework import serializers
from .models import UserBookmarks

class Bookmarkserializer(serializers.ModelSerializer):
	class Meta:
		model = UserBookmarks
		fields = '__all__'
