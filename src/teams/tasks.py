import os
import logging

import django

# Django installed apps must be imported before Models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup(set_prefix=False)

from teams.models import update_team_forecast
from leagues.models import RotoMultiLeagues
from teams.models import YahooTeam, YahooRotoTeam
from stats.models import YahooStats


logger = logging.getLogger(__name__)


def update_team_forecast_task(**kwargs):
    update_team_forecast()


def update_roto_teams(**kwargs):
    for roto_league in RotoMultiLeagues.objects.filter(is_active=True):
        leagues = [league for league in roto_league.leagues.all()]
        if len(leagues)==0:
            continue

        max_point = sum([
            league.teams.count() for league in roto_league.leagues.all()
        ]) - 1
        stat_map = {
            i['yahoo_id']: i for i in YahooStats.league_stats
        }
        stats = {
            stat_map[stat['id']]['stat']: stat_map[stat['id']]['comparator']
            for stat in leagues[0].stats
        }
        for stat, comparator in stats.items():
            order_by = f'-{stat}' if comparator == '>' else stat
            order_teams = YahooTeam.objects.filter(
                league__in=leagues
            ).order_by(order_by)
            point, previous_value, update_teams = max_point, None, []
            for team in order_teams:
                current_value = getattr(team, stat, None)
                if current_value is None:
                    continue

                # Update Rules
                if (previous_value is None or
                    previous_value == current_value
                ):
                    previous_value = current_value
                    update_teams.append(team)
                    continue

                avg_point = sum([
                    point-i for i in range(len(update_teams))
                ]) / len(update_teams)
                for uteam in update_teams:
                    YahooRotoTeam.objects.update_or_create(
                        team=uteam, league=roto_league,
                        defaults={stat: avg_point}
                    )
                point = point - len(update_teams)
                update_teams = [team]
                previous_value = current_value

        for team in roto_league.roto_teams.all():
            team.total_points = sum([
                getattr(team, stat, 0) for stat in stats if isinstance(getattr(team, stat, 0), float)
            ])
            team.save()


if __name__ == '__main__':
    update_team_forecast_task()
