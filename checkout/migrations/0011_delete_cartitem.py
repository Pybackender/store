# Generated by Django 5.1.1 on 2024-10-12 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]