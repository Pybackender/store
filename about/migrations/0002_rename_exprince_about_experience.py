# Generated by Django 5.1.1 on 2024-10-05 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='exprince',
            new_name='experience',
        ),
    ]
