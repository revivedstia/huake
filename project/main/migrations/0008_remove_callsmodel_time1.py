# Generated by Django 4.2.4 on 2023-08-24 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_callsmodel_delete_calls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callsmodel',
            name='time1',
        ),
    ]
