import json

from django.core.management.base import BaseCommand

from leagues.models import YahooLeague, YahooGame
from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.team import Team
from core.utils import get_oauth
from teams.models import YahooTeam

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):        
        games = YahooGame.objects.all()
        for game in games:
            league = League(get_oauth(), '398.l.24668')
            team = Team(get_oauth(), '398.l.24668.t.12')
            roster = team.roster(1,1)
            player_stats = league.player_stats(8762, req_type='season', season=2019)
            print(player_stats)
            roster = team.roster()
            # game.update_model_from_remote()

