from django.contrib import admin

from players.models import YahooPlayer, BaseballPlayer, ZipsStats, SteamerStats


class YahooPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
        'team__league',
        'baseball_player'
    )
    search_fields = ['first_name', 'last_name']


class BaseballPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
    )
    search_fields = ['first_name', 'last_name']


class ZipsStatsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'r', 'h', 'hr', 'rbi', 'bb', 'so', 'avg', 'obp',
                    'slg', 'ops', 'sb',
                    'ip', 'era', 'whip', 'k9', 'bb9', 'ha')
    list_filter = (
        'team',
    )
    search_fields = ['first_name', 'last_name']

admin.site.register(YahooPlayer, YahooPlayerAdmin)
admin.site.register(BaseballPlayer, BaseballPlayerAdmin)
admin.site.register(ZipsStats, ZipsStatsAdmin)
admin.site.register(SteamerStats)
