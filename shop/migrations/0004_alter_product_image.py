# Generated by Django 4.2.5 on 2023-10-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.BinaryField(),
        ),
    ]
