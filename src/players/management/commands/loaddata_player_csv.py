import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from players.models import ZipsStats
from teams.models import YahooTeam


FILES_DIR = os.path.join(settings.BASE_DIR, "players", "fixtures")

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

]

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for stats in STATS_CSV:
            with open(os.path.join(FILES_DIR, stats['file_name']), encoding='utf-8-sig') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    names = row.pop('Name').split(' ')
                    attr = { stats['mapping'][k]: v for k, v in row.items() }
                    attr['first_name'] = names[0]
                    attr['last_name'] = ' '.join(names[1:])
                    obj, created = stats['model'].objects.update_or_create(
                        remote_player_id=attr.pop('remote_player_id'),
                        defaults=attr,
                    )

        teams = [team.save() for team in YahooTeam.objects.all()]
