from django.db import models

from category.models import Category1, Category2

class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu")
    price = models.IntegerField()

    category_1 = models.ForeignKey(Category1,on_delete=models.CASCADE,related_name="menues")
    category_2 = models.ForeignKey(Category2,on_delete=models.CASCADE)
