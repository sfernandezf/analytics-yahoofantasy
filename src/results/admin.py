from django.contrib import admin

from results.models import YahooMatchup


class YahooMatchupAdmin(admin.ModelAdmin):
    ordering = ['week__week_number', 'league']
    list_display = ('league', 'week', 'home_team', 'visitor_team',
                    'home_win', 'home_loss', 'home_draw',
                    'visitor_win', 'visitor_loss', 'visitor_draw')
    list_filter = (
        'league', 'week'
    )

admin.site.register(YahooMatchup, YahooMatchupAdmin)
