# Generated by Django 3.0.3 on 2020-07-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20200718_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahooteamleagueforecast',
            name='bat_stat_order',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Bat Stat Order'),
        ),
        migrations.AddField(
            model_name='yahooteamleagueforecast',
            name='pit_stat_order',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Pit Stat Order'),
        ),
    ]
