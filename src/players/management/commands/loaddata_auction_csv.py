import csv
import os
import logging
import tempfile
from io import TextIOWrapper

from baseball_id import Lookup
import requests

from django.conf import settings
from django.core.management.base import BaseCommand

from teams.models import YahooTeam

from players.models import AuctionBaseballPlayer, BaseballPlayer
from players import utils


FILES_DIR = os.path.join(settings.BASE_DIR, "players", "fixtures")

logger = logging.getLogger(__name__)


STATS = (
    'mAVG', 'mRBI', 'mR', 'mHR', 'mOBP', 'mSLG', 'mOPS', 'mH', 'mSO', 'mBB',
    'mSBCS', 'mSV', 'mERA', 'mWHIP', 'mK9', 'mBB9', 'mKBB', 'mIP', 'mHLD',
    'mQS', 'mSVHLD', 'PTS', 'aPOS', 'Dollars')

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        logger.info('Open auction')
        for stat in ('bat', 'pit' ):
            tf = tempfile.TemporaryFile(mode="w+b")
            request_attrs = utils.get_fangraphs_auction_attrs(stat)
            with requests.request(**request_attrs, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1024):
                    tf.write(chunk)
            tf.seek(0)
            f = TextIOWrapper(tf, encoding='utf-8-sig')

            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                names = row.pop('PlayerName').split(' ')
                player_atts = {
                    'first_name': names[0],
                    'last_name': ' '.join(names[1:]),
                    'team': row.pop('Team'),
                }

                yahoo_id = utils.get_yahoo_player(
                    None,
                    first_name=player_atts['first_name'],
                    last_name=player_atts['last_name']
                )
                if not yahoo_id: continue
                stat_attr = {
                    stat: utils.get_stat_auction(row.get(stat))
                    for stat in STATS
                }
                player_obj = BaseballPlayer.objects.get(remote_player_id=yahoo_id)
                player_stat, created = AuctionBaseballPlayer.objects.update_or_create(
                    baseballplayer=player_obj,
                    defaults=stat_attr,
                )
            f.close()

        teams = [team.save() for team in YahooTeam.objects.all()]
