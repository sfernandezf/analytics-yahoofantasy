from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from teams.models import YahooTeam
from leagues.models import YahooLeagueWeeks, YahooLeague
from results.remotes import YahooMatchupsRemote


class YahooMatchup(RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "Week {} {} vs {}".format(
            str(self.week.week_number), self.home_team.name, self.visitor_team.name)

    field_mapping = {}
    remote_manager = YahooMatchupsRemote()
    children = []

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

    def update_model_from_remote(self, **kwargs):
        """
        model1.model2.model3.name = x
        geattr(model1, 'model2', object), 'name', x)
        :return: remote object
        """
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
            YahooMatchup.objects.update_or_create(
                   **att
            )



