# Generated by Django 3.0.3 on 2020-07-18 03:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_yahooleague_stats'),
        ('players', '0010_delete_auctionbaseballplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionBaseballPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('mAVG', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mRBI', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mR', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mHR', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mOBP', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mSLG', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mOPS', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mH', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mSO', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mBB', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mSBCS', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mSV', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mERA', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mWHIP', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mK9', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mBB9', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mKBB', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mIP', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mHLD', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mQS', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('mSVHLD', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('PTS', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('aPOS', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('Dollars', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('type', models.CharField(choices=[('day', 'Daily'), ('month', 'Month'), ('week', 'Week'), ('year', 'Yearly'), ('custom', 'Custom')], default='year', max_length=256, verbose_name='Type of Stat')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Stats start')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End start')),
                ('is_forecast', models.BooleanField(default=True, verbose_name='It is projected')),
                ('baseballplayer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.BaseballPlayer', verbose_name='Baseball Player')),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.Year')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
