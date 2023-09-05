from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.OrderListView.as_view()),
    path('list/user/', views.UserOrderListView.as_view()),
    path('create/', views.OrderCreateView),
    path('temperature/list/',views.temperatureList.as_view()),
    path('size/list/',views.SizeList.as_view()),
]
