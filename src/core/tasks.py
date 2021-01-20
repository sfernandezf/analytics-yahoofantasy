import os
import logging

import django
from django.conf import settings

import requests


# Django installed apps must be imported before Models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup(set_prefix=False)


logger = logging.getLogger(__name__)


def keep_site_warm():
    ret = requests.get(settings.KEEP_WARM_URL)
    logger.info({
        'status': ret.status_code,
    })
    return True


if __name__ == "__main__":
    keep_site_warm()
