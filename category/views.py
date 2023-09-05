from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import Category1Serializer, Category2Serializer

from .models import Category1, Category2

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class category1ListView(ListAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(category1ListView, self).dispatch(request, *args, **kwargs)

    queryset = Category1.objects.all()
    serializer_class = Category1Serializer

class category2ListView(ListAPIView):
    serializer_class = Category2Serializer
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(category2ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        parent = Category1.objects.get(id = self.kwargs["id"])
        return Category2.objects.filter(parent = parent)

