from django.urls import path

from . import views

urlpatterns = [
    path('category1/list/', views.category1ListView.as_view()),
    path('category2/list/<int:id>/', views.category2ListView.as_view()),
]
