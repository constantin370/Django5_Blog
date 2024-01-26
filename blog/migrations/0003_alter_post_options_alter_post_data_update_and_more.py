# Generated by Django 5.0 on 2024-01-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='data_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
