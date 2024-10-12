# Generated by Django 5.1.1 on 2024-10-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=255)),
                ('apartment', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('create_account', models.BooleanField(default=False)),
                ('different_address', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'checkout',
                'verbose_name_plural': 'checkouts',
            },
        ),
    ]
