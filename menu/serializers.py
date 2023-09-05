from rest_framework import serializers
from .models import Menu
from category.models import Category1
from django.conf import settings

class MenuEasySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ["id","image","name","price"]

    def get_image(self,obj):

        return settings.KIOSK_HOST + str(obj.image)

class MenuCateSerializer(serializers.ModelSerializer):
    menues = MenuEasySerializer(many=True)
    class Meta:
        model = Category1
        fields = ["name","menues"]

class MenuIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"



