# Generated by Django 5.1.1 on 2024-10-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='account/%Y/%m/%d'),
        ),
    ]
