# Generated by Django 4.2.4 on 2023-08-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svayboy', '0005_svayboy_ru_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svayboy',
            name='ru_title',
            field=models.CharField(default='Сваебойная машина ', max_length=50, verbose_name='Название на русском'),
        ),
    ]