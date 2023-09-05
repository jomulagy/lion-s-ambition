from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.MenuListView.as_view()),
    path('list/<int:id>/', views.MenuEasyListView.as_view()),
    path("id/list/",views.MenuAPIView.as_view()),
    path("favorite/list/",views.FavoriteMenuList.as_view()),
]
