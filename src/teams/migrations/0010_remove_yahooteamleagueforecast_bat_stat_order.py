# Generated by Django 3.0.3 on 2020-07-17 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20200717_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yahooteamleagueforecast',
            name='bat_stat_order',
        ),
    ]
