from django.db import models

from menu.models import Menu

class Order(models.Model):
    totalPrice = models.IntegerField()
    is_pack = models.CharField(max_length=10)
    card_com = models.CharField(max_length=100,null = True)
    card_num = models.CharField(max_length=100,null = True)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Temperature(models.Model):
    name = models.CharField(max_length=100)

class Size(models.Model):
    name = models.CharField(max_length=100)

class Option(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)




