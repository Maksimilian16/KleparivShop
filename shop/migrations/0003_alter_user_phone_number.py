# Generated by Django 4.2.5 on 2023-09-25 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)]),
        ),
    ]
