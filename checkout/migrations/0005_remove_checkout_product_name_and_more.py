# Generated by Django 5.1.1 on 2024-10-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_checkout_product_name_checkout_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='quantity',
        ),
    ]
