# Generated by Django 3.0.3 on 2020-06-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20200630_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahooplayer',
            name='baseball_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
