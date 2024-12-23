# Generated by Django 5.1 on 2024-10-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('content', models.CharField(max_length=125)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('position', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Experiense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('number', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
