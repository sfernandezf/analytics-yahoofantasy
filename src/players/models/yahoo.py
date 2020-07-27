from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

from core.mixins.models import (BaseModel, RemoteObjectModelMixin)

from teams.models import YahooTeam
from players.remotes import YahooPlayerRemote
from players.models.baseball import BaseballPlayer


class YahooPlayerLeague(RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "{} {}".format(self.player.first_name, self.player.last_name)

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooPlayerRemote()

    remote_id = models.IntegerField(
        _("Remote Object Id"), null=True, blank=True)

    player = models.ForeignKey(
        'players.BaseballPlayer', verbose_name=_('Yahoo Team'), on_delete=models.CASCADE,
        related_name='leagues')

    team = models.ForeignKey(
        YahooTeam, verbose_name=_('Yahoo Team'), on_delete=models.CASCADE,
        related_name='players')

    editorial_team_full_name = models.CharField(
        _("Professional Team Name"), max_length=1024, blank=True, null=True)

    eligible_positions = JSONField(
        _('Eligible positions'), default=dict, null=True, blank=True)

    def update_model_from_remote(self, **kwargs):
        kwargs['id'] = kwargs['id'] if 'id' in kwargs else self.remote_id
        kwargs['team'] = kwargs['team'] if 'team' in kwargs \
            else getattr(self, 'team', None)
        try:
            player = BaseballPlayer.objects.get(remote_player_id=kwargs['id'])
        except BaseballPlayer.DoesNotExist:
            self.remote_manager.set_credentials(
                kwargs['team'].get_yahoo_credentials())
            remote = self.remote_manager.get_remote_attrs(**kwargs)
            player = BaseballPlayer(
                remote_player_id=remote['id'],
                first_name=remote['first_name'],
                last_name=remote['last_name'],
                team=remote['editorial_team_full_name']
            )
            player.save()
            kwargs.update(remote)
        kwargs.update(player=player)
        for field, value in kwargs.items():
            setattr(self, self.field_mapping.get(field, field), value)
        self.save()
        return self

    def get_yahoo_credentials(self):
        return self.team.league.yahoo_credentials
