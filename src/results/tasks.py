import os
import logging

import django

# Django installed apps must be imported before Models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup(set_prefix=False)

from leagues.models import YahooLeague, YahooLeagueWeeks
from results.models import YahooMatchup


logger = logging.getLogger(__name__)

def update_matchup(**kwargs):
    logger.info('Start Matchup Sync')
    leagues = YahooLeague.objects.filter(is_active=True)
    matchup = YahooMatchup()
    for league in leagues:
        week = league.weeks.filter(is_current_week=True).first()
        kwargs.update(
            parent_id=league.remote_id,
            league=league,
            id=week.week_number
        )
        matchup.update_model_from_remote(**kwargs)


if __name__ == '__main__':
    update_matchup()
