import os
from django.conf import settings

from yahoo_oauth import OAuth2


def changes_detected(instance, fields, skip_new=False):
    model_class = type(instance)

    if instance._state.adding:
        return instance._state.adding and not skip_new

    filter_data = dict((
        (field_name, getattr(instance, field_name))
        for field_name in fields
    ))
    return not model_class.objects.filter(id=instance.id, **filter_data) \
        .exists()