from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.models import YahooLeague, YahooMultiYearLeague, RotoMultiLeagues
from stats.models import StatsCalculatorMixin, YahooStats
from teams.remotes import YahooTeamRemote

from .mixins import TeamResultsMixin


class YahooTeam(TeamResultsMixin, RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "{} {}".format(self.name, str(self.league))

    children = ['players']

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooTeamRemote()

    name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo League'), on_delete=models.CASCADE,
        related_name='teams', null=True, blank=True
    )

    waiver_priority = models.CharField(
        _('Waiver Priority'), max_length=1024, blank=True, null=True)

    manager_nickname = models.CharField(
        _("Manager Nickname"), max_length=1024, blank=True, null=True)

    manager_email = models.CharField(
        _("Manager Email"), max_length=1024, blank=True, null=True)

    def update_model_from_remote(self, **kwargs):
        if not 'id' in kwargs:
            kwargs['id'] = self.remote_id
        super().update_model_from_remote(**kwargs)
        self.update_children_model_from_remote(**kwargs)

    def update_children_model_from_remote(self, **kwargs):
        """
        :return:
        """
        kwargs['remote_id'] = self.remote_id
        for child in self.children:
            model = getattr(getattr(self, child, object), 'model', None)
            if not model:
                continue
            parent_field_name = str(getattr(
                getattr(self, child, object), 'field', None).name)
            child_objects = {
                i.remote_id: i
                for i in getattr(self, child, []).all()
            }
            child_remotes = self.remote_manager.get_children(child, **kwargs)

            # Remove
            for remote_id, instance in child_objects.items():
                if remote_id not in child_remotes:
                    instance.delete()

            # Adding
            for child_remote in child_remotes:
                atts = {
                    'id': child_remote,
                    'parent_id': kwargs.get('remote_id'),
                    parent_field_name: self
                }

                if child_remote not in child_objects.keys():
                    instance = model()
                else:
                    instances = model.objects.filter(remote_id=child_remote)
                    if len(instances) > 1:
                        instances_to_delete = []
                        instances_to_keep = []
                        for i in instances:
                            if getattr(i, parent_field_name) != self:
                                instances_to_delete.append(i)
                            else:
                                instances_to_keep.append(i)
                        for i in instances_to_delete:
                            i.delete()
                        instance = instances_to_keep[0] \
                            if len(instances_to_keep) > 0 else model()
                    else:
                        instance = instances[0]
                instance.update_model_from_remote(**atts)

    def get_yahoo_credentials(self):
        return self.league.yahoo_credentials

    def get_result(self, result_name):
        result = 0
        for matchup in self.matchups_as_home.all():
            result += getattr(matchup, "home_{}".format(result_name), 0)
        for matchup in self.matchups_as_visitors.all():
            result += getattr(matchup, "visitor_{}".format(result_name), 0)
        return result

    @property
    def win(self):
        return self.get_result('win')


class YahooTeamLeagueForecast(TeamResultsMixin, StatsCalculatorMixin, BaseModel):
    yahoo_team = models.OneToOneField(
        YahooTeam, verbose_name=_('Yahoo Team'), on_delete=models.CASCADE,
        related_name='forecast_team', limit_choices_to={'league__is_active': True},
        null=True, blank=True
    )
    stats_results = JSONField(default=dict)

    def get_players(self):
        return self.yahoo_team.players.objects


class YahooRotoTeam(YahooStats):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'league'], name='unique_team_league'
            )
        ]

    team = models.ForeignKey(
        YahooTeam, verbose_name=_('Yahoo Team'), on_delete=models.CASCADE,
        related_name='roto_stats',
        null=True, blank=True
    )
    league = models.ForeignKey(
        RotoMultiLeagues, verbose_name=_('Yahoo League'), on_delete=models.CASCADE,
        related_name='roto_teams', null=True, blank=True
    )
    total_points = models.FloatField(verbose_name=_('Total Points'), default=0)



class YahooMultiLeagueTeam(TeamResultsMixin, BaseModel):
    def __str__(self):
        return "{}".format(self.name)

    name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    league = models.ForeignKey(
        YahooMultiYearLeague, verbose_name=_('Yahoo Multi Year League'),
        on_delete=models.CASCADE,
        related_name='teams')

    teams = models.ManyToManyField(
        YahooTeam, verbose_name=_('Teams'), related_name= 'multi_league_teams'
    )


def update_results(team, rival_team, stat, w, l, d, stats_results):
    home_team_stat = getattr(team, stat['stat'], None)
    rival_team_stat = getattr(rival_team, stat['stat'], None)
    if home_team_stat is None or rival_team_stat is None:
        return w, l, d, stats_results
    if stat['comparator'] == '>':
        if home_team_stat > rival_team_stat:
            w += 1
            stats_results[stat['stat']]['w'] += 1
        elif home_team_stat < rival_team_stat:
            l += 1
            stats_results[stat['stat']]['l'] += 1
        elif home_team_stat == rival_team_stat:
            d += 1
            stats_results[stat['stat']]['d'] += 1
    elif stat['comparator'] == '<':
        if home_team_stat > rival_team_stat:
            l += 1
            stats_results[stat['stat']]['l'] += 1
        elif home_team_stat < rival_team_stat:
            w += 1
            stats_results[stat['stat']]['w'] += 1
        elif home_team_stat == rival_team_stat:
            d += 1
            stats_results[stat['stat']]['d'] += 1
    return w, l, d, stats_results


def update_team_forecast(**kwargs):
    teams = YahooTeamLeagueForecast.objects.all()
    leagues = set()
    for team in teams:
        leagues.add(team.yahoo_team.league)
        team.save()

    stat_map = {
        i['yahoo_id']: i for i in YahooStats.league_stats
    }
    for league in leagues:
        for yahoo_team in league.teams.all():
            if not hasattr(yahoo_team, 'forecast_team'):
                continue
            team = yahoo_team.forecast_team
            team.total_win, team.total_loss, team.total_draw = 0, 0, 0

            # stats = league.stats
            # stats_results = {
            #     stat_map[stat['id']]['stat']: {'w': 0, 'l': 0, 'd': 0}
            #     for stat in stats
            # }
            stats = YahooStats.auction_stats
            stats_results = {
                stat['stat']: {'w': 0, 'l': 0, 'd': 0}
                for stat in stats
            }

            # for matchup in team.yahoo_team.matchups_as_home.all():
            for rival_team in league.teams.exclude(id=yahoo_team.id):
                # visitor_team = matchup.visitor_team.forecast_team
                w, l, d = 0, 0, 0
                for stat in stats:
                    # stat = stat_map.get(stat['id'])
                    w, l, d, stats_results = update_results(
                        team, rival_team.forecast_team, stat, w, l, d,
                        stats_results
                    )
                team.total_win += w
                team.total_loss += l
                team.total_draw += d
            team.stats_results = stats_results
            team.save()
    return