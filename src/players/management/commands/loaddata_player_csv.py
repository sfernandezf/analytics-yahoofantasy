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

from players.models import BaseballPlayer, ZipsStats, \
    SteamerStats, DepthChartsStats, AtcStats, TheBatStats, BaseballAveStats
from players import utils


FILES_DIR = os.path.join(settings.BASE_DIR, "players", "fixtures")

logger = logging.getLogger(__name__)

BAT_CSV_MAP = {
        'Team': 'team',
        'G': 'g',
        'PA': 'pa',
        'AB': 'ab',
        'H': 'h',
        '2B': 'double',
        '3B': 'triple',
        'HR': 'hr',
        'R': 'r',
        'RBI': 'rbi',
        'BB': 'bb',
        'SO': 'so',
        'HBP': 'hbp',
        'SB': 'sb',
        'CS': 'cs',
        'AVG': 'avg',
        'OBP': 'obp',
        'SLG': 'slg',
        'OPS': 'ops',
        'wOBA': 'woba',
        'Fld': 'fld',
        'wRC+': 'wrcplus',
        'BsR': 'bsr',
        'WAR': 'war',
        'ADP': 'adp'
    }

PITCHING_CSV_MAP = {
    'Team': 'team',
    'G': 'gap',
    'W': 'w',
    'L': 'l',
    'ERA': 'era',
    'HLD': 'hld',
    'SV': 'sv',
    'GS': 'gs',
    'IP': 'ip',
    'H': 'ha',
    'ER': 'er',
    'HR': 'hra',
    'SO': 'soa',
    'BB': 'bba',
    'WHIP': 'whip',
    'K/9': 'k9',
    'BB/9': 'bb9',
    'FIP': 'fip',
    'WAR': 'war',
    'ADP': 'adp',
}

STATS_CSV = [
    {
        "name": "zips",
        "file_name": "zips_bat.csv",
        "model": ZipsStats,
        "mapping": BAT_CSV_MAP,
        'stats': 'bat'
    },
    {
        "name": "zips",
        "file_name": "zips_pitch.csv",
        "model": ZipsStats,
        "mapping": PITCHING_CSV_MAP,
        'stats': 'pit'

    },
    {
        "name": "steamer",
        "file_name": "steamer_bat.csv",
        "model": SteamerStats,
        "mapping": BAT_CSV_MAP,
        'stats': 'bat'
    },
    {
        "name": "steamer",
        "file_name": "steamer_pitch.csv",
        "model": SteamerStats,
        "mapping": PITCHING_CSV_MAP,
        'stats': 'pit'

    },
    {
        "name": "fangraphsdc",
        "file_name": "depthcharts_bat.csv",
        "model": DepthChartsStats,
        "mapping": BAT_CSV_MAP,
        'stats': 'bat'
    },
    {
        "name": "fangraphsdc",
        "file_name": "depthcharts_pitch.csv",
        "model": DepthChartsStats,
        "mapping": PITCHING_CSV_MAP,
        'stats': 'pit'
    },
    {
        "name": "atc",
        "file_name": "atc_bat.csv",
        "model": AtcStats,
        "mapping": BAT_CSV_MAP,
        'stats': 'bat'
    },
    {
        "name": "atc",
        "file_name": "atc_pitch.csv",
        "model": AtcStats,
        "mapping": PITCHING_CSV_MAP,
        'stats': 'pit'

    },
    {
        "name": "thebat",
        "file_name": "thebat_bat.csv",
        "model": TheBatStats,
        "mapping": BAT_CSV_MAP,
        'stats': 'bat'
    },
    {
        "name": "thebat",
        "file_name": "thebat_pitch.csv",
        "model": TheBatStats,
        "mapping": PITCHING_CSV_MAP,
        'stats': 'pit'
    },
    {
        "name": "auction",
        "file_name": "auction.csv",
        "model": TheBatStats,
        "mapping": None,
        'stats': None
    },

]

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for stats in STATS_CSV:
            logger.info('Open %s' % stats['file_name'])
            tf = tempfile.TemporaryFile(mode="w+b")
            request_attrs = utils.get_fangraphs_attrs(
                type=stats['name'], stats=stats['stats']
            )
            with requests.request(**request_attrs, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=1024):
                    tf.write(chunk)
            tf.seek(0)
            f = TextIOWrapper(tf, encoding='utf-8-sig')

            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                names = row.pop('Name').split(' ')
                player_atts = {
                    'first_name': names[0],
                    'last_name': ' '.join(names[1:]),
                    'team': row.pop('Team'),
                }

                yahoo_id = utils.get_yahoo_player(
                    row['playerid'],
                    first_name=player_atts['first_name'],
                    last_name=player_atts['last_name']
                )
                if not yahoo_id: continue
                stat_attr = { stats['mapping'][k]: v for k, v in row.items()
                         if k in stats['mapping']}
                player_obj, created = BaseballPlayer.objects.update_or_create(
                    remote_player_id=yahoo_id,
                    defaults=player_atts,
                )
                player_stat, created = stats['model'].objects.update_or_create(
                    baseballplayer=player_obj,
                    defaults=stat_attr,
                )
            f.close()

        logger.info('Calculating player ave stats')
        player_ave_stat = [
            BaseballAveStats.objects.update_or_create(baseballplayer=player)
            for player in BaseballPlayer.objects.all()
        ]
        teams = [team.save() for team in YahooTeam.objects.all()]
