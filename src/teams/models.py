from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.models import YahooLeague
from teams.remotes import YahooTeamRemote


class YahooTeam(RemoteObjectModelMixin, BaseModel):
    """
    """

    def __str__(self):
        return "{}".format(self.name)

    children = ['players']

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooTeamRemote()

    name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo League'), on_delete=models.CASCADE,
        related_name='teams')

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
        kwargs['remote_id'] = self.remote_id
        super().update_children_model_from_remote(**kwargs)