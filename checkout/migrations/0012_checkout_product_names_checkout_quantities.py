# Generated by Django 5.1.1 on 2024-10-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_delete_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='product_names',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='quantities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
