# Generated by Django 5.1.7 on 2025-03-14 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='accounts',
            new_name='social_accounts',
        ),
    ]
