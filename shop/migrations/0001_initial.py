# Generated by Django 4.2.5 on 2023-09-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
