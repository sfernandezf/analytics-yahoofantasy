# Generated by Django 3.0.2 on 2020-06-29 23:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0002_auto_20200629_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='YahooMultiLeagueTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('gp', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('gs', models.FloatField(blank=True, null=True, verbose_name='Games Started')),
                ('avg', models.FloatField(blank=True, null=True, verbose_name='Batting Average')),
                ('obp', models.FloatField(blank=True, null=True, verbose_name='On-base Percentage')),
                ('slg', models.FloatField(blank=True, null=True, verbose_name='Slugging Percentage')),
                ('ab', models.FloatField(blank=True, null=True, verbose_name='At Bats')),
                ('r', models.FloatField(blank=True, null=True, verbose_name='Runs')),
                ('h', models.FloatField(blank=True, null=True, verbose_name='Hits')),
                ('single', models.FloatField(blank=True, null=True, verbose_name='Singles')),
                ('double', models.FloatField(blank=True, null=True, verbose_name='Doubles')),
                ('triple', models.FloatField(blank=True, null=True, verbose_name='Triples')),
                ('hr', models.FloatField(blank=True, null=True, verbose_name='Home Runs')),
                ('rbi', models.FloatField(blank=True, null=True, verbose_name='Runs Batted In')),
                ('sh', models.FloatField(blank=True, null=True, verbose_name='Sacrifice Hits')),
                ('sf', models.FloatField(blank=True, null=True, verbose_name='Sacrifice Flys')),
                ('sb', models.FloatField(blank=True, null=True, verbose_name='Stolen Bases')),
                ('cs', models.FloatField(blank=True, null=True, verbose_name='Caught Stealing')),
                ('bb', models.FloatField(blank=True, null=True, verbose_name='Walks')),
                ('ibb', models.FloatField(blank=True, null=True, verbose_name='Intentional Walks')),
                ('hbp', models.FloatField(blank=True, null=True, verbose_name='Hit By Pitch')),
                ('k', models.FloatField(blank=True, null=True, verbose_name='Strikeouts')),
                ('gidp', models.FloatField(blank=True, null=True, verbose_name='Ground Into Double Play')),
                ('ops', models.FloatField(blank=True, null=True, verbose_name='On-base + Slugging Percentage')),
                ('tb', models.FloatField(blank=True, null=True, verbose_name='Total Bases')),
                ('po', models.FloatField(blank=True, null=True, verbose_name='Put Outs')),
                ('a', models.FloatField(blank=True, null=True, verbose_name='Assists')),
                ('e', models.FloatField(blank=True, null=True, verbose_name='Errors')),
                ('fpct', models.FloatField(blank=True, null=True, verbose_name='Fielding Percentage')),
                ('xbh', models.FloatField(blank=True, null=True, verbose_name='Extra Base Hits')),
                ('nsb', models.FloatField(blank=True, null=True, verbose_name='Net Stolen Bases')),
                ('sbp', models.FloatField(blank=True, null=True, verbose_name='Stolen Base Percentage')),
                ('cyc', models.FloatField(blank=True, null=True, verbose_name='Hitting for the Cycle')),
                ('pa', models.FloatField(blank=True, null=True, verbose_name='Plate Appearances')),
                ('slam', models.FloatField(blank=True, null=True, verbose_name='Grand Slam Home Runs')),
                ('ofa', models.FloatField(blank=True, null=True, verbose_name='Outfield Assists')),
                ('dpt', models.FloatField(blank=True, null=True, verbose_name='Double Plays Turned')),
                ('ci', models.FloatField(blank=True, null=True, verbose_name='Catcher Interference')),
                ('app', models.FloatField(blank=True, null=True, verbose_name='Appearances')),
                ('era', models.FloatField(blank=True, null=True, verbose_name='Earned Run Average')),
                ('whip', models.FloatField(blank=True, null=True, verbose_name='(Walks + Hits) / Innings Pitched')),
                ('w', models.FloatField(blank=True, null=True, verbose_name='Wins')),
                ('l', models.FloatField(blank=True, null=True, verbose_name='Losses')),
                ('cg', models.FloatField(blank=True, null=True, verbose_name='Completed Games')),
                ('sho', models.FloatField(blank=True, null=True, verbose_name='Shutouts')),
                ('sv', models.FloatField(blank=True, null=True, verbose_name='Saves')),
                ('out', models.FloatField(blank=True, null=True, verbose_name='Outs')),
                ('ha', models.FloatField(blank=True, null=True, verbose_name='Hits Allowed')),
                ('tbf', models.FloatField(blank=True, null=True, verbose_name='Total Batters Faced')),
                ('ra', models.FloatField(blank=True, null=True, verbose_name='Runs Allowed')),
                ('er', models.FloatField(blank=True, null=True, verbose_name='Earned Runs')),
                ('hra', models.FloatField(blank=True, null=True, verbose_name='Home Runs Allowed')),
                ('bba', models.FloatField(blank=True, null=True, verbose_name='Walks Allowed')),
                ('ibba', models.FloatField(blank=True, null=True, verbose_name='Intentional Walks Allowed')),
                ('hbpa', models.FloatField(blank=True, null=True, verbose_name='Hit Batters')),
                ('ka', models.FloatField(blank=True, null=True, verbose_name='Strikeouts Allowed')),
                ('wp', models.FloatField(blank=True, null=True, verbose_name='Wild Pitches')),
                ('blk', models.FloatField(blank=True, null=True, verbose_name='Balks')),
                ('sba', models.FloatField(blank=True, null=True, verbose_name='Stolen Bases Allowed')),
                ('gidpa', models.FloatField(blank=True, null=True, verbose_name='Batters Grounded Into Double Plays')),
                ('svop', models.FloatField(blank=True, null=True, verbose_name='Save Chances')),
                ('hld', models.FloatField(blank=True, null=True, verbose_name='Holds')),
                ('k9', models.FloatField(blank=True, null=True, verbose_name='Strikeouts per Nine Innings')),
                ('kbb', models.FloatField(blank=True, null=True, verbose_name='Strikeout to Walk Ratio')),
                ('tba', models.FloatField(blank=True, null=True, verbose_name='Total Bases Allowed')),
                ('ip', models.FloatField(blank=True, null=True, verbose_name='Innings Pitched')),
                ('pc', models.FloatField(blank=True, null=True, verbose_name='Pitch Count')),
                ('doublea', models.FloatField(blank=True, null=True, verbose_name='Doubles Allowed')),
                ('triplea', models.FloatField(blank=True, null=True, verbose_name='Triples Allowed')),
                ('rw', models.FloatField(blank=True, null=True, verbose_name='Relief Wins')),
                ('rl', models.FloatField(blank=True, null=True, verbose_name='Relief Losses')),
                ('pick', models.FloatField(blank=True, null=True, verbose_name='Pickoffs')),
                ('rapp', models.FloatField(blank=True, null=True, verbose_name='Relief Appearances')),
                ('obpa', models.FloatField(blank=True, null=True, verbose_name='On-base Percentage Against')),
                ('winp', models.FloatField(blank=True, null=True, verbose_name='Winning Percentage')),
                ('singlea', models.FloatField(blank=True, null=True, verbose_name='Singles Allowed')),
                ('h9', models.FloatField(blank=True, null=True, verbose_name='Hits Per Nine Innings')),
                ('bb9', models.FloatField(blank=True, null=True, verbose_name='Walks Per Nine Innings')),
                ('nh', models.FloatField(blank=True, null=True, verbose_name='No Hitters')),
                ('pg', models.FloatField(blank=True, null=True, verbose_name='Perfect Games')),
                ('svp', models.FloatField(blank=True, null=True, verbose_name='Save Percentage')),
                ('ira', models.FloatField(blank=True, null=True, verbose_name='Inherited Runners Scored')),
                ('qs', models.FloatField(blank=True, null=True, verbose_name='Quality Starts')),
                ('bsv', models.FloatField(blank=True, null=True, verbose_name='Blown Saves')),
                ('nsv', models.FloatField(blank=True, null=True, verbose_name='Net Saves')),
                ('total_win', models.IntegerField(default=0, verbose_name='Team League W')),
                ('total_loss', models.IntegerField(default=0, verbose_name='Team League L')),
                ('total_draw', models.IntegerField(default=0, verbose_name='Team League D')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='leagues.YahooMultiYearLeague', verbose_name='Yahoo Multi Yearr League')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YahooTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('remote_id', models.CharField(blank=True, max_length=1024, null=True, unique=True, verbose_name='Remote Object Id')),
                ('gp', models.FloatField(blank=True, null=True, verbose_name='Games Played')),
                ('gs', models.FloatField(blank=True, null=True, verbose_name='Games Started')),
                ('avg', models.FloatField(blank=True, null=True, verbose_name='Batting Average')),
                ('obp', models.FloatField(blank=True, null=True, verbose_name='On-base Percentage')),
                ('slg', models.FloatField(blank=True, null=True, verbose_name='Slugging Percentage')),
                ('ab', models.FloatField(blank=True, null=True, verbose_name='At Bats')),
                ('r', models.FloatField(blank=True, null=True, verbose_name='Runs')),
                ('h', models.FloatField(blank=True, null=True, verbose_name='Hits')),
                ('single', models.FloatField(blank=True, null=True, verbose_name='Singles')),
                ('double', models.FloatField(blank=True, null=True, verbose_name='Doubles')),
                ('triple', models.FloatField(blank=True, null=True, verbose_name='Triples')),
                ('hr', models.FloatField(blank=True, null=True, verbose_name='Home Runs')),
                ('rbi', models.FloatField(blank=True, null=True, verbose_name='Runs Batted In')),
                ('sh', models.FloatField(blank=True, null=True, verbose_name='Sacrifice Hits')),
                ('sf', models.FloatField(blank=True, null=True, verbose_name='Sacrifice Flys')),
                ('sb', models.FloatField(blank=True, null=True, verbose_name='Stolen Bases')),
                ('cs', models.FloatField(blank=True, null=True, verbose_name='Caught Stealing')),
                ('bb', models.FloatField(blank=True, null=True, verbose_name='Walks')),
                ('ibb', models.FloatField(blank=True, null=True, verbose_name='Intentional Walks')),
                ('hbp', models.FloatField(blank=True, null=True, verbose_name='Hit By Pitch')),
                ('k', models.FloatField(blank=True, null=True, verbose_name='Strikeouts')),
                ('gidp', models.FloatField(blank=True, null=True, verbose_name='Ground Into Double Play')),
                ('ops', models.FloatField(blank=True, null=True, verbose_name='On-base + Slugging Percentage')),
                ('tb', models.FloatField(blank=True, null=True, verbose_name='Total Bases')),
                ('po', models.FloatField(blank=True, null=True, verbose_name='Put Outs')),
                ('a', models.FloatField(blank=True, null=True, verbose_name='Assists')),
                ('e', models.FloatField(blank=True, null=True, verbose_name='Errors')),
                ('fpct', models.FloatField(blank=True, null=True, verbose_name='Fielding Percentage')),
                ('xbh', models.FloatField(blank=True, null=True, verbose_name='Extra Base Hits')),
                ('nsb', models.FloatField(blank=True, null=True, verbose_name='Net Stolen Bases')),
                ('sbp', models.FloatField(blank=True, null=True, verbose_name='Stolen Base Percentage')),
                ('cyc', models.FloatField(blank=True, null=True, verbose_name='Hitting for the Cycle')),
                ('pa', models.FloatField(blank=True, null=True, verbose_name='Plate Appearances')),
                ('slam', models.FloatField(blank=True, null=True, verbose_name='Grand Slam Home Runs')),
                ('ofa', models.FloatField(blank=True, null=True, verbose_name='Outfield Assists')),
                ('dpt', models.FloatField(blank=True, null=True, verbose_name='Double Plays Turned')),
                ('ci', models.FloatField(blank=True, null=True, verbose_name='Catcher Interference')),
                ('app', models.FloatField(blank=True, null=True, verbose_name='Appearances')),
                ('era', models.FloatField(blank=True, null=True, verbose_name='Earned Run Average')),
                ('whip', models.FloatField(blank=True, null=True, verbose_name='(Walks + Hits) / Innings Pitched')),
                ('w', models.FloatField(blank=True, null=True, verbose_name='Wins')),
                ('l', models.FloatField(blank=True, null=True, verbose_name='Losses')),
                ('cg', models.FloatField(blank=True, null=True, verbose_name='Completed Games')),
                ('sho', models.FloatField(blank=True, null=True, verbose_name='Shutouts')),
                ('sv', models.FloatField(blank=True, null=True, verbose_name='Saves')),
                ('out', models.FloatField(blank=True, null=True, verbose_name='Outs')),
                ('ha', models.FloatField(blank=True, null=True, verbose_name='Hits Allowed')),
                ('tbf', models.FloatField(blank=True, null=True, verbose_name='Total Batters Faced')),
                ('ra', models.FloatField(blank=True, null=True, verbose_name='Runs Allowed')),
                ('er', models.FloatField(blank=True, null=True, verbose_name='Earned Runs')),
                ('hra', models.FloatField(blank=True, null=True, verbose_name='Home Runs Allowed')),
                ('bba', models.FloatField(blank=True, null=True, verbose_name='Walks Allowed')),
                ('ibba', models.FloatField(blank=True, null=True, verbose_name='Intentional Walks Allowed')),
                ('hbpa', models.FloatField(blank=True, null=True, verbose_name='Hit Batters')),
                ('ka', models.FloatField(blank=True, null=True, verbose_name='Strikeouts Allowed')),
                ('wp', models.FloatField(blank=True, null=True, verbose_name='Wild Pitches')),
                ('blk', models.FloatField(blank=True, null=True, verbose_name='Balks')),
                ('sba', models.FloatField(blank=True, null=True, verbose_name='Stolen Bases Allowed')),
                ('gidpa', models.FloatField(blank=True, null=True, verbose_name='Batters Grounded Into Double Plays')),
                ('svop', models.FloatField(blank=True, null=True, verbose_name='Save Chances')),
                ('hld', models.FloatField(blank=True, null=True, verbose_name='Holds')),
                ('k9', models.FloatField(blank=True, null=True, verbose_name='Strikeouts per Nine Innings')),
                ('kbb', models.FloatField(blank=True, null=True, verbose_name='Strikeout to Walk Ratio')),
                ('tba', models.FloatField(blank=True, null=True, verbose_name='Total Bases Allowed')),
                ('ip', models.FloatField(blank=True, null=True, verbose_name='Innings Pitched')),
                ('pc', models.FloatField(blank=True, null=True, verbose_name='Pitch Count')),
                ('doublea', models.FloatField(blank=True, null=True, verbose_name='Doubles Allowed')),
                ('triplea', models.FloatField(blank=True, null=True, verbose_name='Triples Allowed')),
                ('rw', models.FloatField(blank=True, null=True, verbose_name='Relief Wins')),
                ('rl', models.FloatField(blank=True, null=True, verbose_name='Relief Losses')),
                ('pick', models.FloatField(blank=True, null=True, verbose_name='Pickoffs')),
                ('rapp', models.FloatField(blank=True, null=True, verbose_name='Relief Appearances')),
                ('obpa', models.FloatField(blank=True, null=True, verbose_name='On-base Percentage Against')),
                ('winp', models.FloatField(blank=True, null=True, verbose_name='Winning Percentage')),
                ('singlea', models.FloatField(blank=True, null=True, verbose_name='Singles Allowed')),
                ('h9', models.FloatField(blank=True, null=True, verbose_name='Hits Per Nine Innings')),
                ('bb9', models.FloatField(blank=True, null=True, verbose_name='Walks Per Nine Innings')),
                ('nh', models.FloatField(blank=True, null=True, verbose_name='No Hitters')),
                ('pg', models.FloatField(blank=True, null=True, verbose_name='Perfect Games')),
                ('svp', models.FloatField(blank=True, null=True, verbose_name='Save Percentage')),
                ('ira', models.FloatField(blank=True, null=True, verbose_name='Inherited Runners Scored')),
                ('qs', models.FloatField(blank=True, null=True, verbose_name='Quality Starts')),
                ('bsv', models.FloatField(blank=True, null=True, verbose_name='Blown Saves')),
                ('nsv', models.FloatField(blank=True, null=True, verbose_name='Net Saves')),
                ('total_win', models.IntegerField(default=0, verbose_name='Team League W')),
                ('total_loss', models.IntegerField(default=0, verbose_name='Team League L')),
                ('total_draw', models.IntegerField(default=0, verbose_name='Team League D')),
                ('name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Team Name')),
                ('waiver_priority', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Waiver Priority')),
                ('manager_nickname', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Manager Nickname')),
                ('manager_email', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Manager Email')),
                ('league', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='leagues.YahooLeague', verbose_name='Yahoo League')),
                ('multiyear_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leagues', to='teams.YahooMultiLeagueTeam', verbose_name='Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
