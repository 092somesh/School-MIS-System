# Generated by Django 5.0.2 on 2024-03-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_car_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='speed',
            field=models.IntegerField(default=50),
        ),
    ]
