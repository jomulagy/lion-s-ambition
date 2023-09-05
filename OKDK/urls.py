from django.urls import path
from .views import *

urlpatterns = [
    path("signal/",SignalAPIView.as_view()),
]
