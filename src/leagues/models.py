from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.remotes import YahooLeagueRemote, YahooGameRemote, YahooWeeksRemote


class YahooGame(RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "{} {}".format(self.code, str(self.year))
    
    field_mapping = {}
    remote_manager = YahooGameRemote()
    children = ['leagues']

    code = models.CharField(
        _("Game Code"), max_length=128, default='mlb')

    year = models.IntegerField(_("Fantasy Game year"))

    def update_model_from_remote(self, **kwargs):
        kwargs['code'] = self.code
        super().update_model_from_remote(**kwargs)
        self.update_children_model_from_remote(**kwargs)

    def update_children_model_from_remote(self, **kwargs):
        kwargs['code'] = self.code
        kwargs['year'] = self.year
        super().update_children_model_from_remote(**kwargs)


class YahooLeague(RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "{}".format(self.name)
    children = [
        'weeks',
        'teams',
        'matchups'
    ]
    
    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooLeagueRemote()
        
    name = models.CharField(
        _("League Name"), max_length=1024, blank=True, null=True)

    game = models.ForeignKey(
        YahooGame, verbose_name=_('Yahoo Game'), on_delete=models.CASCADE,
        related_name='leagues')

    current_week = models.IntegerField(
        _('Current Week'), blank=True, null=True)

    draft_status = models.CharField(
        _("Draft Status"), max_length=1024, blank=True, null=True)

    num_teams = models.IntegerField(
        _('Number of Teams'), blank=True, null=True)

    league_type = models.CharField(
        _("League Type"), max_length=1024, blank=True, null=True)

    playoff_start_week = models.IntegerField(
        _('Playoff Start Week'), blank=True, null=True)

    def update_model_from_remote(self, **kwargs):
        if not 'id' in kwargs:
            kwargs['id'] = self.remote_id
        super().update_model_from_remote(**kwargs)
        self.update_children_model_from_remote(**kwargs)

    def update_children_model_from_remote(self, **kwargs):
        kwargs['remote_id'] = self.remote_id
        super().update_children_model_from_remote(**kwargs)


class YahooLeagueWeeks(RemoteObjectModelMixin, BaseModel):
    def __str__(self):
        return "{}".format(self.week_number)

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooWeeksRemote()

    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo Game'), on_delete=models.CASCADE,
        related_name='weeks')

    week_number = models.IntegerField(_('Week Number'), blank=True, null=True)

    start_date = models.DateField(_('Start Date'), blank=True, null=True)

    end_date = models.DateField(_('End Date'), blank=True, null=True)

    is_current_week = models.BooleanField(_('Is Current Week'), default=False)