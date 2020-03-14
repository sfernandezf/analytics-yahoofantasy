from django.contrib import admin

from players.models import YahooPlayer


class YahooPlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team')
    list_filter = (
        'team',
        'team__league'
    )


admin.site.register(YahooPlayer, YahooPlayerAdmin)
