# Generated by Django 3.0.3 on 2020-07-01 00:46

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20200630_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahooleague',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Meta'),
        ),
    ]