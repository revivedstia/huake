# Generated by Django 4.2.4 on 2023-08-23 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_calls_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calls',
            name='time',
        ),
    ]