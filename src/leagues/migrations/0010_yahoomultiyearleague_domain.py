# Generated by Django 3.0.3 on 2020-07-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0009_yahooleague_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahoomultiyearleague',
            name='domain',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Domain'),
        ),
    ]
