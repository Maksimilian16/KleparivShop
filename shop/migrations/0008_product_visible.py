# Generated by Django 4.2.5 on 2023-10-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_customuser_password_alter_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]