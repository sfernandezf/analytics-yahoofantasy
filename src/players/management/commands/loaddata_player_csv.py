import csv
import os
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from players.models import BaseballPlayer, ZipsStats, \
    SteamerStats, DepthChartsStats, AtcStats, TheBatStats, BaseballAveStats
from teams.models import YahooTeam


FILES_DIR = os.path.join(settings.BASE_DIR, "players", "fixtures")

logger = logging.getLogger(__name__)

BAT_CSV_MAP = {
        'playerid': 'remote_player_id',
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
    'playerid': 'remote_player_id',
    'Team': 'team',
    'G': 'g',
    'W': 'w',
    'L': 'l',
    'ERA': 'era',
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
        "mapping": BAT_CSV_MAP
    },
    {
        "name": "zips",
        "file_name": "zips_pitch.csv",
        "model": ZipsStats,
        "mapping": PITCHING_CSV_MAP

    },
    {
        "name": "steamer",
        "file_name": "steamer_bat.csv",
        "model": SteamerStats,
        "mapping": BAT_CSV_MAP
    },
    {
        "name": "steamer",
        "file_name": "steamer_pitch.csv",
        "model": SteamerStats,
        "mapping": PITCHING_CSV_MAP

    },
    {
        "name": "depthcharts",
        "file_name": "depthcharts_bat.csv",
        "model": DepthChartsStats,
        "mapping": BAT_CSV_MAP
    },
    {
        "name": "depthcharts",
        "file_name": "depthcharts_pitch.csv",
        "model": DepthChartsStats,
        "mapping": PITCHING_CSV_MAP
    },
    {
        "name": "atc",
        "file_name": "atc_bat.csv",
        "model": AtcStats,
        "mapping": BAT_CSV_MAP
    },
    {
        "name": "atc",
        "file_name": "atc_pitch.csv",
        "model": AtcStats,
        "mapping": PITCHING_CSV_MAP

    },
    {
        "name": "thebat",
        "file_name": "thebat_bat.csv",
        "model": TheBatStats,
        "mapping": BAT_CSV_MAP
    },
    {
        "name": "thebat",
        "file_name": "thebat_pitch.csv",
        "model": TheBatStats,
        "mapping": PITCHING_CSV_MAP
    }
]

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for stats in STATS_CSV:
            logger.info('Open %s' % stats['file_name'])
            with open(os.path.join(FILES_DIR, stats['file_name']), encoding='utf-8-sig') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    # logger.info('Rows in %s are %s' % (stats['file_name'], str(row)))
                    names = row.pop('Name').split(' ')
                    player_atts = {
                        'first_name': names[0],
                        'last_name': ' '.join(names[1:]),
                        'team':  row.pop('Team'),
                        'remote_player_id': row.pop('playerid')
                    }

                    stat_attr = { stats['mapping'][k]: v for k, v in row.items()
                             if k in stats['mapping']}
                    player_obj, created = BaseballPlayer.objects.update_or_create(
                        remote_player_id=player_atts.pop('remote_player_id'),
                        defaults=player_atts,
                    )
                    player_stat, created = stats['model'].objects.update_or_create(
                        baseballplayer=player_obj,
                        defaults=stat_attr,
                    )

        logger.info('Calculating player ave stats')
        player_ave_stat = [
            BaseballAveStats.objects.update_or_create(baseballplayer=player)
            for player in BaseballPlayer.objects.all()
        ]
        teams = [team.save() for team in YahooTeam.objects.all()]
