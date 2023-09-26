from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    __tablename__ = 'shop_user'
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=9, validators=[MinLengthValidator(9)])
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=255)
