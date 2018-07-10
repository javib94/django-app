from django.db import models

# Create your models here.


class Product(models.Model):
    name_id = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    price = models.DoubleField(default=0)


