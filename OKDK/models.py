from django.db import models

# Create your models here.
class Signal(models.Model):
    status = models.BooleanField(default = False)
