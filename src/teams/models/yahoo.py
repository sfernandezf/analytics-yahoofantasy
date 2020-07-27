from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.models import YahooLeague, YahooMultiYearLeague
from stats.models import StatsCalculatorMixin
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
        related_name='teams', null=True, blank=True)

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
            child_objects = getattr(self, child, []).all().values('remote_id')
            child_remotes = self.remote_manager.get_children(child, **kwargs)
            child_objects_list = [k['remote_id'] for k in child_objects]

            for child_remote in child_remotes:
                atts = {
                    'id': child_remote,
                    'parent_id': kwargs.get('remote_id'),
                    parent_field_name: self
                }

                if child_remote not in child_objects_list:
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
        related_name='forecast_team', limit_choices_to={'league__is_active': True})

    def get_players(self):
        return self.yahoo_team.players.objects


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

