from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.utils import changes_detected

from players.models import YahooPlayerLeague
from teams.models import (
    YahooMultiLeagueTeam, YahooTeam, update_team_forecast, YahooRotoTeam
)


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

    from stats.models import YahooStats
    yahoo_stats = YahooStats.league_stats
    for multi_team in instance.multi_league_teams.all():
        multi_team.total_win, multi_team.total_loss, multi_team.total_draw = 0, 0, 0
        for team in multi_team.teams.all():
            multi_team.total_win += team.total_win
            multi_team.total_loss += team.total_loss
            multi_team.total_draw += team.total_draw
            for stat in yahoo_stats:
                stat_name = stat['stat']
                stat_value = getattr(team, stat_name, None)
                if stat_value is None:
                    continue
                setattr(multi_team, stat_name, stat_value)
        multi_team.w_pct = (multi_team.total_win + 0.5 * multi_team.total_draw) / (multi_team.total_win + multi_team.total_draw + multi_team.total_loss)
        multi_team.save()
    return


# @receiver(post_save, sender=YahooPlayerLeague)
# def on_yahoo_player_league_update__update_forecast_league(instance, **kwargs):
#     """
#     """
#     if 'team' in (kwargs.get('update_fields', []) or []):
#         update_team_forecast()


@receiver(post_save, sender=YahooTeam)
def on_yahoo_team_created__create_roto(instance, **kwargs):
    if instance._state.adding is False:
        return
    YahooPlayerLeague.objects.get_or_create(
        team=instance
    )
