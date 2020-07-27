import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from players.models import BaseballPlayer, YahooPlayerLeague


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for yahoo_player in YahooPlayerLeague.objects.filter(player__baseballavestats__g=None):
            print(yahoo_player)
            # baseball_player = BaseballPlayer.objects.filter(
            #     first_name__unaccent__icontains=yahoo_player.first_name,
            #     last_name__unaccent__icontains=yahoo_player.last_name).first()
            # yahoo_player.baseball_player = baseball_player
            # yahoo_player.save()