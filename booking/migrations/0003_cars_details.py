# Generated by Django 5.1.7 on 2025-03-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_accounts_social_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_booking', models.CharField(max_length=100)),
                ('car_details', models.CharField(max_length=100)),
            ],
        ),
    ]
