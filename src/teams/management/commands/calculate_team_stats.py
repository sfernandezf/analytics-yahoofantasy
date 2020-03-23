from django.core.management.base import BaseCommand

from teams.models import YahooTeam

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):        
        teams = YahooTeam.objects.all()
        for team in teams:
            team.save()

