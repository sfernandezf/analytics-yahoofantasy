# Generated by Django 3.0.3 on 2021-04-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0021_auto_20210427_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahoorototeam',
            name='total_points',
            field=models.FloatField(default=0, verbose_name='Total Points'),
        ),
    ]