from django.core.management.base import BaseCommand

from teams.models import update_team_forecast

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        update_team_forecast()
