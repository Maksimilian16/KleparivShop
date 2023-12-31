# Generated by Django 4.2.5 on 2023-10-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_customuser_alter_user_name_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.customuser'),
        ),
    ]
