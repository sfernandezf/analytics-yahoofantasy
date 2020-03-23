from django.contrib import admin

from leagues.models import YahooLeague, YahooGame, YahooLeagueWeeks


class YahooLeagueWeeksAdmin(admin.ModelAdmin):
    ordering = ['league', 'week_number']
    list_display = ('__str__', 'league', 'is_current_week')
    list_filter = (
        'league', 'is_current_week'
    )


admin.site.register(YahooGame)
admin.site.register(YahooLeague)

admin.site.register(YahooLeagueWeeks, YahooLeagueWeeksAdmin)