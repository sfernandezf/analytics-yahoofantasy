import os
import logging

import django

# Django installed apps must be imported before Models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup(set_prefix=False)

from teams.models import update_team_forecast


logger = logging.getLogger(__name__)


def update_team_forecast_task(**kwargs):
    update_team_forecast()


if __name__ == '__main__':
    update_team_forecast_task()
