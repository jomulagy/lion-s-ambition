from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

class Category1(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category2(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Category1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

