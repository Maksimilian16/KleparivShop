from django.db import models


class User(models.Model):
    __table__ = "shop_user"
    phone_number = models.CharField(max_length=20)  # Adjust max_length as needed
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=12)


class Product(models.Model):
    __table__ = "shop_product"
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=160)
    price = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
