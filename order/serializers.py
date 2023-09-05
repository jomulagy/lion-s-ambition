from rest_framework import serializers
from .models import Temperature, Size, Option, Order
from menu.models import Menu
from django.conf import settings

class MenuSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ["name","image","price"]

    def get_image(self,obj):
        return obj.image.url

class OrderSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M:%S")
    class Meta:
        model = Order
        fields = ["id","brand","options","created_at","totalPrice"]

    def get_brand(self,instance):
        return "OKDK"

    def get_options(self,instance):
        options = OptionSerializer(instance.option_set.all(),many=True).data
        return options

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ["id","name"]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id","name"]

class OptionSerializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField()
    temperature = serializers.CharField(source = "temperature.name")
    size = serializers.CharField(source = "size.name")
    class Meta:
        model = Option
        fields = ["menu", "temperature","size","quantity"]

    def get_menu(self,obj):
        return MenuSerializer(obj.menu).data
