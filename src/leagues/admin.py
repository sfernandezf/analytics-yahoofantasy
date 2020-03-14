from django.contrib import admin

from leagues.models import YahooLeague, YahooGame

# Register your models here.

admin.site.register(YahooGame)
admin.site.register(YahooLeague)