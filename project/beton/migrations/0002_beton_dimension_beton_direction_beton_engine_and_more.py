# Generated by Django 4.2.4 on 2023-08-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beton',
            name='dimension',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Габариты'),
        ),
        migrations.AddField(
            model_name='beton',
            name='direction',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Формальное направление'),
        ),
        migrations.AddField(
            model_name='beton',
            name='engine',
            field=models.CharField(blank=True, default='500', max_length=50, null=True, verbose_name='Двигатель'),
        ),
        migrations.AddField(
            model_name='beton',
            name='lifting',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Подъемная способность'),
        ),
        migrations.AddField(
            model_name='beton',
            name='stop',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Тормозная система'),
        ),
        migrations.AddField(
            model_name='beton',
            name='tire',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Размер шин'),
        ),
        migrations.AddField(
            model_name='beton',
            name='transmission',
            field=models.CharField(blank=True, default='Ручная механическая коробка', max_length=50, null=True, verbose_name='Коробка передач'),
        ),
        migrations.AddField(
            model_name='beton',
            name='water_supply',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Способ подачи воды'),
        ),
        migrations.AlterField(
            model_name='beton',
            name='state',
            field=models.CharField(default='под заказ', max_length=50, verbose_name='Состояние'),
        ),
    ]