from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import MenuEasySerializer, MenuCateSerializer, MenuIDSerializer
from rest_framework.response import Response
from django.conf import settings

import requests

from .models import Menu
from category.models import Category1, Category2
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class MenuListView(APIView):
    def get(self,request):
        categories = Category1.objects.filter(id__gte = '3')
        datas = MenuCateSerializer(categories,many=True).data
        return Response(status = 200,data = datas)

class MenuEasyListView(ListAPIView):
    serializer_class = MenuEasySerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(MenuEasyListView, self).dispatch(request, *args, **kwargs)
    def get_queryset(self):
        category = Category2.objects.get(id = self.kwargs["id"])
        return Menu.objects.filter(category_2 = category)

class MenuAPIView(APIView):
    def get(self,request):
        data = MenuIDSerializer(Menu.objects.all(),many = True).data
        return Response(data)


class FavoriteMenuList(APIView):
    def get(self,request):
        if 'HTTP_AUTHORIZATION' in request.META:
            access_token = request.META.get('HTTP_AUTHORIZATION')
            if access_token:
                api = getattr(settings,"APP_HOST")
                header = {
                    "Authorization" : access_token
                }
                print(api+"order/favorite/")
                print(requests.get(api+"order/favorite/",headers=header))
                print(requests.get(api+"order/favorite/",headers=header).json())

                # try:
                #     res = requests.get(api+"order/favorite/",headers=header)
                #     favorites = res.json()["username"]
                # except:
                #     return Response(data = res.text)
                favorites = requests.get(api+"order/favorite/",headers=header).json()
                return Response(favorites)
        else:
            return Response(status = 401, data = {"message" : "accessToken 없음"})
