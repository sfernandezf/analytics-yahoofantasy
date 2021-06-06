from django.contrib import admin

from leagues.models import (
    YahooLeague, YahooGame, YahooLeagueWeeks, YahooMultiYearLeague, Year,
    YahooOauthCredentials, RotoMultiLeagues
)


class YahooLeagueAdmin(admin.ModelAdmin):
    ordering = ['year', 'name']
    list_display = ('name', 'year', 'current_week')
    list_filter = (
        'league', 'year'
    )


class YahooLeagueWeeksAdmin(admin.ModelAdmin):
    ordering = ['league', 'week_number']
    list_display = ('__str__', 'league', 'is_current_week')
    list_filter = (
        'league', 'is_current_week'
    )


class RotoMultiLeaguesAdmin(admin.ModelAdmin):
    filter_horizontal = ('leagues',)


admin.site.register(YahooOauthCredentials)
admin.site.register(Year)
admin.site.register(YahooGame)
admin.site.register(YahooLeague)
admin.site.register(YahooMultiYearLeague)

admin.site.register(YahooLeagueWeeks, YahooLeagueWeeksAdmin)
admin.site.register(RotoMultiLeagues, RotoMultiLeaguesAdmin)