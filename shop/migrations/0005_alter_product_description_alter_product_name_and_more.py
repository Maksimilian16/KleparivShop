# Generated by Django 4.2.5 on 2023-10-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
