# Generated by Django 3.0.3 on 2021-06-05 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210605_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='end_datetime',
            new_name='end_timestamp',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='start_datetime',
            new_name='start_timestamp',
        ),
    ]