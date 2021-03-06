# Generated by Django 3.0.3 on 2020-07-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_baseballplayer_eligible_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='atcstats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='atcstats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='baseballavestats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='baseballavestats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='depthchartsstats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='depthchartsstats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='steamerstats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='steamerstats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='thebatstats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='thebatstats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='zipsstats',
            name='hld',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
        migrations.AddField(
            model_name='zipsstats',
            name='sv',
            field=models.FloatField(blank=True, null=True, verbose_name='SV'),
        ),
    ]
