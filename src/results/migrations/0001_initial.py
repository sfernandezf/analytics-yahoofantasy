# Generated by Django 3.0.2 on 2020-06-29 23:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0002_auto_20200629_2319'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YahooMatchup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('remote_id', models.CharField(blank=True, max_length=1024, null=True, unique=True, verbose_name='Remote Object Id')),
                ('home_win', models.IntegerField(default=0)),
                ('home_loss', models.IntegerField(default=0)),
                ('home_draw', models.IntegerField(default=0)),
                ('visitor_win', models.IntegerField(default=0)),
                ('visitor_loss', models.IntegerField(default=0)),
                ('visitor_draw', models.IntegerField(default=0)),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchups_as_home', to='teams.YahooTeam', verbose_name='Yahoo Home Team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchups', to='leagues.YahooLeague', verbose_name='Yahoo League')),
                ('visitor_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchups_as_visitors', to='teams.YahooTeam', verbose_name='Yahoo Visitor Team')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchups', to='leagues.YahooLeagueWeeks', verbose_name='Yahoo Week')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
