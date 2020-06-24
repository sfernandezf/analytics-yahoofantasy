from django.contrib import admin

from results.models import YahooMatchup


class YahooMatchupAdmin(admin.ModelAdmin):
    ordering = ['week__week_number', 'league']
    list_display = ('league', 'week', 'home_team', 'visitor_team')
    list_filter = (
        'league', 'week'
    )

admin.site.register(YahooMatchup, YahooMatchupAdmin)
