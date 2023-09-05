from rest_framework import serializers
from .models import Category1, Category2

class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = "__all__"

class Category2Serializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()
    class Meta:
        model = Category2
        fields = "__all__"


