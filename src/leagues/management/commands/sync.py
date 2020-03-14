import json

from django.core.management.base import BaseCommand

from leagues.models import YahooLeague, YahooGame
from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.team import Team
from core.utils import get_oauth


class Command(BaseCommand):
    help = 'Dump auth groups and permissions in custom format'

    def handle(self, *args, **options):
        games = YahooGame.objects.all()
        for game in games:
            # league = League(get_oauth(), '398.l.24668')
            # team = Team(get_oauth(), '398.l.24668.t.12')
            # taken_player = league.taken_players()
            # roster = team.roster()
            game.update_model_from_remote()
