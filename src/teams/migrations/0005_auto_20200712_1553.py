# Generated by Django 3.0.3 on 2020-07-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_yahooleague_stats'),
        ('teams', '0004_auto_20200706_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='yahoomultileagueteam',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Team Name'),
        ),
        migrations.AlterField(
            model_name='yahoomultileagueteam',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='leagues.YahooMultiYearLeague', verbose_name='Yahoo Multi Year League'),
        ),
    ]
