# Generated by Django 5.0 on 2024-01-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_data_update_alter_post_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_update',
            field=models.DateField(blank=True, null=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
