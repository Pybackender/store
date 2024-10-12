# Generated by Django 5.1.1 on 2024-10-12 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='checkout.checkout')),
            ],
        ),
    ]