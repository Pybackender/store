# Generated by Django 5.1.1 on 2024-10-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_info_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.URLField(blank=True, null=True),
        ),
    ]
