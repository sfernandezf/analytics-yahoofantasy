from django.contrib import admin

from players.models import YahooPlayerLeague, BaseballPlayer, ZipsStats, \
    SteamerStats, DepthChartsStats, AtcStats, TheBatStats, BaseballAveStats, \
    AuctionBaseballPlayer


class YahooPlayerLeagueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team__league__game__year',
        'team__league',
        'team',
    )
    raw_id_fields = ('player', )
    search_fields = ['player__first_name', 'player__last_name']


class YahooLeaguesInline(admin.TabularInline):
    model = YahooPlayerLeague


class BaseballPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
        'leagues__team'
    )
    search_fields = ['first_name', 'last_name']
    # raw_id_fields = ('leagues',)
    inlines = [YahooLeaguesInline]
#
#
class PlayerAvailable(admin.SimpleListFilter):
    title = 'player available'
    parameter_name = 'is_available'

    def lookups(self, request, model_admin):
        return (
            ('True', True),
            ('False', False),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value in ['True', 'False']:
            value = value == 'True'
            return queryset.filter(baseballplayer__leagues__isnull=value)
        return queryset


class IsPitcherFilter(admin.SimpleListFilter):
    title = 'Is Pitcherr'
    parameter_name = 'is_pitcher'
    stat_name = 'h'

    def lookups(self, request, model_admin):
        return (
            ('True', True),
            ('False', False),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value in ['True', 'False']:
            value = value == 'True'
            return queryset.filter(**{f'{self.stat_name}__isnull': value})
        return queryset


class IsRegularPlyaer(admin.SimpleListFilter):
    title = 'Is Regular'
    parameter_name = 'is_regular'
    stat_name = 'pa'

    def lookups(self, request, model_admin):
        return (
            ('True', True),
            ('False', False),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value in ['True', 'False']:
            if value == 'True':
                return queryset.filter(**{f'{self.stat_name}__gt': 330})
            else:
                return queryset.filter(**{f'{self.stat_name}__lte': 330})
        return queryset


class YahooLeaguesInline2(admin.TabularInline):
    model = YahooPlayerLeague
    fk_name = 'player__auctionbaseballplayer'


class BaseStatsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pa', 'r', 'h', 'hr', 'rbi', 'bb', 'so', 'avg', 'obp',
                    'slg', 'ops', 'sb',
                    'ip', 'era', 'whip', 'k9', 'bb9', 'ha', 'adp')
    list_filter = (
        'baseballplayer__team',
        'baseballplayer__leagues__team',
        PlayerAvailable,
        IsPitcherFilter,
        IsRegularPlyaer
    )
    search_fields = ['baseballplayer__first_name', 'baseballplayer__last_name']
    # inlines = [YahooLeaguesInline2]


class ZipsStatsAdmin(BaseStatsAdmin):
    pass


class SteamerStatsAdmin(BaseStatsAdmin):
    pass


class DephthChartsStatsAdmin(BaseStatsAdmin):
    pass


class AtcStatsAdmin(BaseStatsAdmin):
    pass


class TheBatStatsAdmin(BaseStatsAdmin):
    pass


class BaseballAveStatsAdmin(BaseStatsAdmin):
    pass


class AuctionIsPitcherFilter(IsPitcherFilter):
    stat_name = 'mH'


class AuctionBaseballPlayerAdmin(BaseStatsAdmin):
    list_display = ('__str__', ) + (
        'mAVG', 'mRBI', 'mR', 'mHR', 'mOBP', 'mSLG', 'mOPS', 'mH', 'mSO', 'mBB',
        'mSBCS', 'mSV', 'mERA', 'mWHIP', 'mK9', 'mBB9', 'mKBB', 'mIP', 'mHLD',
        'mQS', 'mSVHLD', 'PTS', 'aPOS', 'Dollars'
    )
    list_filter = (
        'baseballplayer__team',
        'baseballplayer__leagues__team',
        PlayerAvailable,
        AuctionIsPitcherFilter,
        IsRegularPlyaer
    )


admin.site.register(YahooPlayerLeague, YahooPlayerLeagueAdmin)
admin.site.register(BaseballPlayer, BaseballPlayerAdmin)
admin.site.register(ZipsStats, ZipsStatsAdmin)
admin.site.register(SteamerStats, SteamerStatsAdmin)
admin.site.register(DepthChartsStats, DephthChartsStatsAdmin)
admin.site.register(AtcStats, AtcStatsAdmin)
admin.site.register(TheBatStats, TheBatStatsAdmin)
admin.site.register(BaseballAveStats, BaseballAveStatsAdmin)
admin.site.register(AuctionBaseballPlayer, AuctionBaseballPlayerAdmin)

