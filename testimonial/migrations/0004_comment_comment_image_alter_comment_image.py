# Generated by Django 5.1.1 on 2024-10-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0003_alter_experiense_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comment/%Y/%m/%d'),
        ),
    ]
