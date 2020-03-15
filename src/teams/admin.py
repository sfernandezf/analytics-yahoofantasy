from django.contrib import admin

from teams.models import YahooTeam


class YahooTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'manager_nickname', 'waiver_priority','ip', 'era', 'whip', 'k9', 'bb9', 'h9', 'rapp', 'kbb')
    list_filter = (
        'league',
    )


admin.site.register(YahooTeam, YahooTeamAdmin)
