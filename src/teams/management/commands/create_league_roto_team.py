from django.core.management.base import BaseCommand

from teams.tasks import update_roto_teams


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        update_roto_teams()
