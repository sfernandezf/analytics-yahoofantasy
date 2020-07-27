from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.models import YahooLeagueWeeks, YahooLeague
from results.remotes import YahooMatchupsRemote
from stats.models import YahooStats
from teams.models import YahooTeam


class MatchupMixin(models.Model):
    """
    """
    class Meta:
        abstract = True

    home_win = models.IntegerField(default=0)
    home_loss = models.IntegerField(default=0)
    home_draw = models.IntegerField(default=0)
    visitor_win = models.IntegerField(default=0)
    visitor_loss = models.IntegerField(default=0)
    visitor_draw = models.IntegerField(default=0)


class YahooMatchupTeamResult(YahooStats, BaseModel):
    def __str__(self):
        return str(
            {
                i: getattr(self, i)
                for i in self.stat_list
                if getattr(self, i, None)
            }
        )


class YahooMatchup(MatchupMixin, RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "Week {} {} vs {}".format(
            str(self.week.week_number), self.home_team.name, self.visitor_team.name)

    field_mapping = {}
    remote_manager = YahooMatchupsRemote()
    children = []

    updated_result_timestamp = models.DateTimeField(_("Created At"), null=True)
    home_team = models.ForeignKey(
        YahooTeam, verbose_name=_('Yahoo Home Team'), on_delete=models.CASCADE,
        related_name='matchups_as_home')
    visitor_team = models.ForeignKey(
        YahooTeam, verbose_name=_('Yahoo Visitor Team'), on_delete=models.CASCADE,
        related_name='matchups_as_visitors')
    week = models.ForeignKey(
        YahooLeagueWeeks, verbose_name=_('Yahoo Week'),
        on_delete=models.CASCADE,
        related_name='matchups')
    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo League'),
        on_delete=models.CASCADE,
        related_name='matchups')

    home_results = models.ForeignKey(
        YahooMatchupTeamResult,
        verbose_name=_('Home Team Results'),
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    visitor_results = models.ForeignKey(
        YahooMatchupTeamResult,
        verbose_name=_('Visitor Team Results'),
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    def update_model_from_remote(self, **kwargs):
        self.remote_manager.set_credentials(
            kwargs['league'].get_yahoo_credentials())
        matchups = self.remote_manager.get_remote_attrs(**kwargs)
        for matchup in matchups:
            att = {
                'home_team': YahooTeam.objects.get(
                    remote_id=matchup['home_team']),
                'visitor_team': YahooTeam.objects.get(
                    remote_id=matchup['visitor_team']),
                'week': YahooLeagueWeeks.objects.get(
                    week_number=matchup['week'], league=kwargs['league']),
                'league': kwargs['league']
            }
            matchup_instance, _ = YahooMatchup.objects.update_or_create(
                   **att
            )

            # Update Stats
            matchup_instance.updated_result_timestamp = timezone.now()
            home_results = matchup_instance.home_results or YahooMatchupTeamResult()
            visitor_results = matchup_instance.visitor_results or YahooMatchupTeamResult()

            stat_map = {
                i['yahoo_id']:i for i in YahooStats.league_stats
            }
            for stat in matchup_instance.league.stats:

                setattr(
                    home_results,
                    stat_map.get(stat['id'])['stat'],
                    self.__convert_stat(matchup['home_team_stats'].get(str(stat['id'])))
                )
                setattr(
                    visitor_results,
                    stat_map.get(stat['id'])['stat'],
                    self.__convert_stat(matchup['visitor_team_stats'].get(str(stat['id'])))
                )
            home_results.save()
            visitor_results.save()
            matchup_instance.home_results = home_results
            matchup_instance.visitor_results = visitor_results
            matchup_instance.save()

    def get_yahoo_credentials(self):
        return self.league.yahoo_credentials

    def __convert_stat(self, stat):
        try:
            return float(stat)
        except ValueError:
            return None



