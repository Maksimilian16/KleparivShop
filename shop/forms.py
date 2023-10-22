from django import forms
from django.db import models


class Products(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    photo = forms.ImageField()


class User(models.Model):
    __table__ = "shop_user"
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=12)
