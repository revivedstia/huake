# Generated by Django 4.2.4 on 2023-08-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', models.IntegerField(verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('message', models.CharField(max_length=250, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Заявка на звонок',
                'verbose_name_plural': 'Заявки на звонки',
            },
        ),
        migrations.CreateModel(
            name='Ekskavator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('ru_title', models.CharField(default='Погрузчик', max_length=50, verbose_name='Название на русском')),
                ('state', models.CharField(default='под заказ', max_length=50, verbose_name='Состаяние')),
                ('prise', models.IntegerField(default=0, verbose_name='Цена')),
                ('image1', models.ImageField(upload_to='imag/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='imag/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='imag/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='imag/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='imag/')),
            ],
            options={
                'verbose_name': 'Погрузчик',
                'verbose_name_plural': 'Погрузчики',
            },
        ),
    ]
