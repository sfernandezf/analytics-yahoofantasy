from django.db import models
from django.utils.translation import ugettext_lazy as _

from stats.models import YahooStats, AuctionStats


class TeamResultsMixin(YahooStats, AuctionStats, models.Model):
    class Meta:
        abstract = True

    total_win = models.IntegerField(_('Team League W'), default=0)
    total_loss = models.IntegerField(_('Team League L'), default=0)
    total_draw = models.IntegerField(_('Team League D'), default=0)
    w_pct = models.FloatField(_('w_pct'), default=0)

    @property
    def w(self):
        return self.total_win or 0

    @property
    def l(self):
        return self.total_loss or 0

    @property
    def d(self):
        return self.total_draw or 0

    @property
    def pct(self):
       return '{:.3f}'.format(self.w_pct, 3).lstrip('0')

