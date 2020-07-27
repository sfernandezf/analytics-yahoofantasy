from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.utils import changes_detected

from teams.models import YahooMultiLeagueTeam, YahooTeam


@receiver(post_save, sender=YahooTeam)
def on_yahoo_result_updated_update_multi_league(instance, **kwargs):
    """
    """
    is_changed = changes_detected(
        instance,
        fields=('total_win', 'total_draw', 'total_loss',),
        skip_new=False
    )
    if len(instance.multi_league_teams.all())==0:
        return

    for multi_team in instance.multi_league_teams.all():
        multi_team.total_win, multi_team.total_loss, multi_team.total_draw = 0, 0, 0
        for team in multi_team.teams.all():
            multi_team.total_win += team.total_win
            multi_team.total_loss += team.total_loss
            multi_team.total_draw += team.total_draw
        multi_team.save()
    return