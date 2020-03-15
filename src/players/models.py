from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

from core.mixins.models import (BaseModel, RemoteObjectModelMixin, BaseStats)

from leagues.models import YahooLeague
from teams.models import YahooTeam
from players.remotes import YahooPlayerRemote


class YahooPlayer(RemoteObjectModelMixin, BaseModel):
    """
    """

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooPlayerRemote()

    remote_id = models.IntegerField(
        _("Remote Object Id"), null=True, blank=True)

    first_name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    last_name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    team = models.ForeignKey(
        YahooTeam, verbose_name=_('Yahoo Team'), on_delete=models.CASCADE,
        related_name='players')


    editorial_team_full_name = models.CharField(
        _("Professional Team Name"), max_length=1024, blank=True, null=True)

    eligible_positions = JSONField(
        _('Eligible positions'), default=dict, null=True, blank=True)

    baseball_player = models.ForeignKey(
        'BaseballPlayer', on_delete=models.SET_NULL, null=True, blank=True)
    
    def update_model_from_remote(self, **kwargs):
        kwargs['id'] = kwargs['id'] if 'id' in kwargs else self.remote_id
        kwargs['team'] = kwargs['team'] if 'team' in kwargs \
            else getattr(self, 'team', None)
        super().update_model_from_remote(**kwargs)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

class BaseballPlayer(BaseModel):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    first_name = models.CharField(
        _("First Name"), max_length=1024, blank=True, null=True)

    last_name = models.CharField(
        _("Last Name"), max_length=1024, blank=True, null=True)

    team = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)
    
    remote_player_id = models.CharField(
        _("Remote Player Id"), max_length=1024, blank=True, null=True, unique=True)


class ZipsStats(BaseStats, BaseballPlayer):
    pass


class SteamerStats(BaseStats, BaseballPlayer):
    pass






