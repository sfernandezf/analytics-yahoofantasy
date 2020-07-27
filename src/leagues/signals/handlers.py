from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.utils import changes_detected

from leagues.models import YahooLeague


@receiver(pre_save, sender=YahooLeague)
def on_yahoo_league_updated(instance, **kwargs):
    """
    """
    is_changed = changes_detected(
        instance, fields=('game', 'yahoo_credentials'), skip_new=False)
    if not is_changed or \
        instance.yahoo_credentials is None or instance.game is None:
        return instance
    instance.remote_manager.set_credentials(instance.get_yahoo_credentials())
    instance.meta = instance.get_leagues()
    return instance

