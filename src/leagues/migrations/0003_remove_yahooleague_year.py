# Generated by Django 3.0.3 on 2020-06-30 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20200629_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yahooleague',
            name='year',
        ),
    ]