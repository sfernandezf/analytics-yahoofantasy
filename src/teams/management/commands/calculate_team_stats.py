from django.core.management.base import BaseCommand

from teams.models import YahooTeamLeagueForecast
from stats.models import YahooStats

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):        
        teams = YahooTeamLeagueForecast.objects.all()
        leagues = set()
        for team in teams:
            leagues.add(team.yahoo_team.league)
            team.save()

        stat_map = {
            i['yahoo_id']: i for i in YahooStats.league_stats
        }
        for league in leagues:
            for yahoo_team in league.teams.all():
                if not hasattr(yahoo_team, 'forecast_team'):
                    continue
                team = yahoo_team.forecast_team
                team.total_win, team.total_loss, team.total_draw = 0, 0, 0
                for matchup in team.yahoo_team.matchups_as_home.all():
                    visitor_team = matchup.visitor_team.forecast_team
                    matchup_win, matchup_loss, matchup_draw = 0, 0, 0
                    for stat in league.stats:
                        stat = stat_map.get(stat['id'])
                        home_team_stat = getattr(team, stat['stat'], None)
                        visitor_team_stat = getattr(visitor_team, stat['stat'], None)
                        if home_team_stat is None or visitor_team_stat is None:
                            continue

                        if stat['comparator'] == '>':
                            if home_team_stat > visitor_team_stat:
                                matchup_win += 1
                            elif home_team_stat < visitor_team_stat:
                                matchup_loss += 1
                            elif home_team_stat == visitor_team_stat:
                                matchup_draw += 1

                        elif stat['comparator'] == '<':
                            if home_team_stat > visitor_team_stat:
                                matchup_loss += 1
                            elif home_team_stat < visitor_team_stat:
                                matchup_win += 1
                            elif home_team_stat == visitor_team_stat:
                                matchup_draw += 1
                    team.total_win += matchup_win
                    team.total_loss += matchup_loss
                    team.total_draw += matchup_draw

                for matchup in team.yahoo_team.matchups_as_visitors.all():
                    home_team = matchup.home_team.forecast_team
                    matchup_win, matchup_loss, matchup_draw = 0, 0, 0
                    for stat in league.stats:
                        stat = stat_map.get(stat['id'])
                        home_team_stat = getattr(home_team, stat['stat'], None)
                        visitor_team_stat = getattr(team, stat['stat'], None)
                        if home_team_stat is None or visitor_team_stat is None:
                            continue

                        if stat['comparator'] == '>':
                            if home_team_stat > visitor_team_stat:
                                matchup_loss += 1
                            elif home_team_stat < visitor_team_stat:
                                matchup_win += 1
                            elif home_team_stat == visitor_team_stat:
                                matchup_draw += 1

                        elif stat['comparator'] == '<':
                            if home_team_stat > visitor_team_stat:
                                matchup_win += 1
                            elif home_team_stat < visitor_team_stat:
                                matchup_loss += 1
                            elif home_team_stat == visitor_team_stat:
                                matchup_draw += 1
                    team.total_win += matchup_win
                    team.total_loss += matchup_loss
                    team.total_draw += matchup_draw

                team.save()
        return

