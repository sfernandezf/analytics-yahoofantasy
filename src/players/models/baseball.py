from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

from core.mixins.models import BaseModel
from stats.models import BaseStats, AuctionStats


class BaseballPlayer(BaseModel):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    first_name = models.CharField(
        _("First Name"), max_length=1024, blank=True, null=True)

    last_name = models.CharField(
        _("Last Name"), max_length=1024, blank=True, null=True)

    team = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    remote_player_id = models.CharField(
        _("Remote Player Id"), max_length=1024, blank=True, null=True,
        unique=True)

    eligible_positions = JSONField(
        _('Eligible positions'), default=dict, null=True, blank=True)


    def calculate_value(self, *args):
        value = 0
        for arg in args:
            stat = getattr(self.auctionbaseballplayer, arg, None)
            if stat:
                value += stat
        return value


class BaseBaseballStat(BaseModel):
    class Meta:
        abstract = True

    def __str__(self):
        return "{} {}".format(
            self.baseballplayer.first_name, self.baseballplayer.last_name)

    baseballplayer = models.OneToOneField(
        BaseballPlayer, verbose_name=_('Baseball Player'), unique=True,
        on_delete=models.CASCADE)

    STATS_TYPE_CHOICES = (
        ('day', 'Daily'),
        ('month', 'Month'),
        ('week', 'Week'),
        ('year', 'Yearly'),
        ('custom', 'Custom'),
    )
    type = models.CharField(
        _('Type of Stat'), choices=STATS_TYPE_CHOICES, max_length=256,
        default='year')
    start_date = models.DateField(_('Stats start'), null=True, blank=True)
    end_date = models.DateField(_('End start'), null=True, blank=True)
    is_forecast = models.BooleanField(_('It is projected'), default=True)
    year = models.ForeignKey(
        'leagues.Year', on_delete=models.CASCADE, null=True, blank=True)


class ZipsStats(BaseStats, BaseBaseballStat):
    pass


class SteamerStats(BaseStats, BaseBaseballStat):
    pass


class DepthChartsStats(BaseStats, BaseBaseballStat):
    pass


class AtcStats(BaseStats, BaseBaseballStat):
    pass


class TheBatStats(BaseStats, BaseBaseballStat):
    pass


class BaseballAveStats(BaseStats, BaseBaseballStat):
    def save(self, *args, **kwargs):
        average_stats = [
            SteamerStats, DepthChartsStats, AtcStats, TheBatStats
        ]
        for stat in self.stat_list:
            stats = [getattr(
                getattr(self.baseballplayer, source._meta.model_name, object),
                stat, None) for source in average_stats]
            stats = [i for i in stats if i]
            average = sum(stats) / len(stats) if len(stats) > 0 else None
            setattr(self, stat, average)
        super().save(*args, **kwargs)


class AuctionBaseballPlayer(AuctionStats, BaseBaseballStat):
    pass