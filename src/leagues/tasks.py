import os
import logging

import django

# Django installed apps must be imported before Models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup(set_prefix=False)

from leagues.models import YahooLeague


logger = logging.getLogger(__name__)


def update_entire_league(**kwargs):
    logger.info('Start League Sync')
    leagues = YahooLeague.objects.filter(is_active=True)
    for league in leagues:
        league.update_model_from_remote(**kwargs)


if __name__ == '__main__':
    update_entire_league()
