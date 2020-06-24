from django.contrib import admin

from teams.models import YahooTeam


class YahooTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'manager_nickname', 'waiver_priority','r', 'h', 'hr', 'rbi', 'bb', 'so', 'avg', 'obp', 'slg', 'ops', 'nsb', 'ip', 'era', 'whip', 'kbb', 'k9', 'rapp', 'h9', 'bb9')
    list_filter = (
        'league',
    )


admin.site.register(YahooTeam, YahooTeamAdmin)
