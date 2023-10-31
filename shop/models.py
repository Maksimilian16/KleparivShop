from django.db import models


class CustomUser(models.Model):
    phone_number = models.CharField(max_length=13)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=32)


class Product(models.Model):
    visible = models.BooleanField(default=True)
    image = models.BinaryField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
