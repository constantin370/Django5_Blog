# Generated by Django 5.0 on 2024-03-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_prof_union'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Определяет, следует ли считать этого пользователя активным. Снимите этот флажок вместо удаления учетных записей.', verbose_name='active'),
        ),
    ]
