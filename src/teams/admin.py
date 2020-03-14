from django.contrib import admin

from teams.models import YahooTeam


class YahooTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'manager_nickname', 'waiver_priority')
    list_filter = (
        'league',
    )


admin.site.register(YahooTeam, YahooTeamAdmin)
