# Generated by Django 3.0.3 on 2020-07-17 00:47
from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20200630_0210'),
    ]

    operations = [
        UnaccentExtension()
    ]
