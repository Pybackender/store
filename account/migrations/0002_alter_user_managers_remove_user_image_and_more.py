# Generated by Django 5.1.1 on 2024-10-06 08:16

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='read',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]