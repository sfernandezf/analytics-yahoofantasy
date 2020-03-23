from django.contrib import admin

from players.models import YahooPlayer, BaseballPlayer, ZipsStats, \
    SteamerStats, DepthChartsStats, AtcStats, TheBatStats, BaseballAveStats


class YahooPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
        'team__league'
    )
    search_fields = ['first_name', 'last_name']


class BaseballPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
    )
    search_fields = ['first_name', 'last_name']


class BaseStatsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'r', 'h', 'hr', 'rbi', 'bb', 'so', 'avg', 'obp',
                    'slg', 'ops', 'sb',
                    'ip', 'era', 'whip', 'k9', 'bb9', 'ha')
    list_filter = (
        'baseballplayer__team',
    )
    search_fields = ['baseballplayer__first_name', 'baseballplayer__last_name']
    
    
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

admin.site.register(YahooPlayer, YahooPlayerAdmin)
admin.site.register(BaseballPlayer, BaseballPlayerAdmin)
admin.site.register(ZipsStats, ZipsStatsAdmin)
admin.site.register(SteamerStats, SteamerStatsAdmin)
admin.site.register(DepthChartsStats, DephthChartsStatsAdmin)
admin.site.register(AtcStats, AtcStatsAdmin)
admin.site.register(TheBatStats, TheBatStatsAdmin)
admin.site.register(BaseballAveStats, BaseballAveStatsAdmin)

