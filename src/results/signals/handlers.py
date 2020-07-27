from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.utils import changes_detected
from stats.models import YahooStats

from results.models import YahooMatchup, YahooMatchupTeamResult


@receiver(pre_save, sender=YahooMatchup)
def on_yahoo_result_updated_update_result_wins(instance, **kwargs):
    """
    """
    is_changed = changes_detected(
        instance, fields=('updated_result_timestamp', ), skip_new=False)
    if not is_changed:
        return
    instance.home_win, instance.home_loss, instance.home_draw = 0, 0, 0
    instance.visitor_win, instance.visitor_loss, instance.visitor_draw = 0, 0, 0
    home_team_results = instance.home_results
    visitor_team_results = instance.visitor_results
    stat_map = {
        i['yahoo_id']: i for i in YahooStats.league_stats
    }
    for stat in instance.league.stats:
        stat = stat_map.get(stat['id'])
        home_team_stat = getattr(
            home_team_results, stat['stat'], None)
        visitor_team_stat = getattr(
            visitor_team_results,stat['stat'], None)
        if home_team_stat is None or visitor_team_stat is None:
            continue
        if stat['comparator'] == '>':
            if home_team_stat > visitor_team_stat:
                instance.home_win += 1
                instance.visitor_loss += 1
            elif home_team_stat < visitor_team_stat:
                instance.home_loss += 1
                instance.visitor_win += 1
            elif home_team_stat == visitor_team_stat:
                instance.home_draw += 1
                instance.visitor_draw += 1
        elif stat['comparator'] == '<':
            if home_team_stat > visitor_team_stat:
                instance.home_loss += 1
                instance.visitor_win += 1
            elif home_team_stat < visitor_team_stat:
                instance.home_win += 1
                instance.visitor_loss += 1
            elif home_team_stat == visitor_team_stat:
                instance.home_draw += 1
                instance.visitor_draw += 1

    return instance


@receiver(post_save, sender=YahooMatchup)
def on_yahoo_result_updated_update_teams_wins(instance, **kwargs):
    """
    """
    is_changed = changes_detected(
        instance,
        fields=('home_win', 'home_draw', 'home_loss', 'visitor_win',
                'visitor_draw', 'visitor_loss'),
        skip_new=False
    )
    # if not is_changed:
    #     return

    home_team = instance.home_team
    visitor_team = instance.visitor_team
    for team in (home_team, visitor_team):
        team.total_win, team.total_loss, team.total_draw = 0, 0, 0
        for matchup in team.matchups_as_home.all():
            team.total_win += matchup.home_win
            team.total_loss += matchup.home_loss
            team.total_draw += matchup.home_draw
        for matchup in team.matchups_as_visitors.all():
            team.total_win += matchup.visitor_win
            team.total_loss += matchup.visitor_loss
            team.total_draw += matchup.visitor_draw
        team.save()
    return