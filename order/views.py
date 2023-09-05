import requests
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, Option, Temperature, Size
from menu.models import Menu
from .serializers import TemperatureSerializer, SizeSerializer, OptionSerializer, OrderSerializer
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

class OrderListView(APIView):
    def post(self,request):
        user = request.data["user"]
        data = Order.objects.filter(user = user).order_by("-created_at")
        data = OrderSerializer(data,many = True).data
        return Response(data)

class UserOrderListView(APIView):
    def post(self,request):
        user = request.data["user"]
        data = Order.objects.filter(user = user).order_by("-created_at")
        data = OrderSerializer(data,many = True).data
        return Response(data)

@csrf_exempt
def OrderCreateView(request):
    if request.method == "POST":
        access_token = request.META.get('HTTP_AUTHORIZATION')
        if access_token:
            api = getattr(settings,"APP_HOST")
            header = {
                "Authorization" : access_token
            }
            user = requests.get(api+"account/user/",headers=header).json()['user']["username"]
            card_data = requests.get(api+"account/user/default/card/",headers=header)
            if card_data.status_code == 200:
                card_data = card_data.json()
            else:
                return JsonResponse({'error': '유효하지 않은 Access 토큰'}, status=401)
            params = {"brand": "OKDK"}
            membership = requests.get(api+"account/user/membership/",headers=header,params = params)
            if membership.status_code == 200:
                membership = membership.json()
            else:
                return JsonResponse({'error': '유효하지 않은 Access 토큰'}, status=401)

        context = json.loads(request.body)

        total_price = 0
        order = Order.objects.create(is_pack = context["is_pack"],totalPrice=0,user = user)
        if access_token and card_data:
            order.card_com = card_data["name"]
            order.card_num = card_data["serial_num"]
        order.save()

        for data in context["data"]:
            option = Option()
            option.quantity = data["quantity"]
            menu = Menu.objects.get(name = data["name"])
            option.temperature = Temperature.objects.get(name = data["temperature"])
            option.size = Size.objects.get(name = data["size"])
            option.order = order
            option.menu = menu
            option.save()

            total_price += menu.price * option.quantity
        order.totalPrice = total_price
        order.save()
        options = order.option_set.all()
        options = OptionSerializer(options,many = True)
        if access_token:

            data = {
                "brand" : "OKDK",
                "point" : order.totalPrice * 0.1,
                "type" : "적립"
            }

            requests.post(api+"payment/membership/history/",json = data,headers=header)
        return JsonResponse({"order_num":order.id})

class temperatureList(APIView):
    def get(self,request):
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures,many=True)

        return Response(serializer.data)

class SizeList(APIView):
    def get(self,request):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes,many=True)

        return Response(serializer.data)
