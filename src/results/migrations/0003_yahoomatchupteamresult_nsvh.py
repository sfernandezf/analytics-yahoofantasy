# Generated by Django 3.0.3 on 2020-07-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20200630_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahoomatchupteamresult',
            name='nsvh',
            field=models.FloatField(blank=True, null=True, verbose_name='Net Saves or Holds'),
        ),
    ]