# Generated by Django 3.0.3 on 2020-07-17 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_yahoomatchupteamresult_nsvh'),
        ('players', '0006_auto_20200717_0047'),
        ('teams', '0006_auto_20200712_1641'),
    ]

    operations = [
        migrations.DeleteModel(
            name='YahooTeamLeagueForecast',
        ),
    ]
