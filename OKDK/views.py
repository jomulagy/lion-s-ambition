from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response

from .models import Signal

@permission_classes((AllowAny,))
class SignalAPIView(APIView):
    SIGNAL = False
    def get(self,request):
        SIGNAL = Signal.objects.get(id = "1")
        print(SIGNAL.status)
        return Response(SIGNAL.status)

    def post(self,request):
        SIGNAL = Signal.objects.get(id = "1")
        if request.data["signal"][0] == "1":
            SIGNAL.status = True
            SIGNAL.save()
        else:
            SIGNAL.status = False
            SIGNAL.save()
        print(SIGNAL.status)
        return Response(status=200)


