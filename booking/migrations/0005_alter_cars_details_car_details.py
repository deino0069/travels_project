# Generated by Django 5.1.7 on 2025-03-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_cars_details_car_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars_details',
            name='car_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
