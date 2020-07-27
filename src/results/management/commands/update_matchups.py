import json

from django.core.management.base import BaseCommand

from leagues.models import YahooLeague
from results.models import YahooMatchup
from teams.models import YahooTeam

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):        
        matchups = YahooMatchup.objects.all()
        teams = YahooTeam.objects.all()
        for matchup in matchups:
            matchup.home_win = 0
            matchup.home_loss = 0
            matchup.home_draw = 0
            matchup.visitor_win = 0
            matchup.visitor_loss = 0
            matchup.visitor_draw = 0
            home_team = matchup.home_team
            visitor_team = matchup.visitor_team
            for stat in matchup.league.league_stats:
                home_team_stat = getattr(home_team.home_results, stat['stat'], None)
                visitor_team_stat = getattr(visitor_team, stat['stat'], None)
                if stat['comparator'] == '>':
                    if home_team_stat > visitor_team_stat:
                        matchup.home_win +=1
                        matchup.visitor_loss +=1
                    elif home_team_stat < visitor_team_stat:
                        matchup.home_loss += 1
                        matchup.visitor_win += 1
                    elif home_team_stat == visitor_team_stat:
                        matchup.home_draw += 1
                        matchup.visitor_draw += 1
                elif stat['comparator'] == '<':
                    if home_team_stat > visitor_team_stat:
                        matchup.home_loss +=1
                        matchup.visitor_win +=1
                    elif home_team_stat < visitor_team_stat:
                        matchup.home_win += 1
                        matchup.visitor_loss += 1
                    elif home_team_stat == visitor_team_stat:
                        matchup.home_draw += 1
                        matchup.visitor_draw += 1
            matchup.save()

        for team in teams:
            team.total_win = 0
            team.total_loss = 0
            team.total_draw = 0
            for matchup in team.matchups_as_home.all():
                team.total_win += matchup.home_win
                team.total_loss += matchup.home_loss
                team.total_draw += matchup.home_draw
            for matchup in team.matchups_as_visitors.all():
                team.total_win += matchup.visitor_win
                team.total_loss += matchup.visitor_loss
                team.total_draw += matchup.visitor_draw
            team.save()
