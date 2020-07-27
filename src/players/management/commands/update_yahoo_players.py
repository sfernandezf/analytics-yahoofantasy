from django.core.management.base import BaseCommand

from leagues.models import YahooLeague
from players.models import BaseballPlayer


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        leagues = YahooLeague.objects.filter(is_active=True)
        for league in leagues:
            league.update_players_from_remote()

