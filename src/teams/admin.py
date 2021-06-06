from django.contrib import admin

from core.admin import JSONFieldWidgetAdminMixin

from teams.models import (
    YahooTeam, YahooTeamLeagueForecast, YahooMultiLeagueTeam, YahooRotoTeam
)


class YahooTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'manager_nickname', 'waiver_priority', 'win', 'total_win', 'total_loss', 'total_draw',)
    list_filter = ('league',)


class YahooTeamLeagueForecastAdmin(JSONFieldWidgetAdminMixin, admin.ModelAdmin):
    list_display = (
        'yahoo_team', 'total_win', 'total_loss', 'total_draw', 'avg' ,'r', 'h',
        'hr', 'rbi', 'bb','k','obp', 'slg', 'ops', 'nsb', 'ip', 'era', 'whip',
        'kbb', 'k9', 'bb9', 'h9', 'rapp', 'sv', 'hld', 'mR', 'mH',
        'mHR', 'mRBI', 'mBB', 'mSO', 'mAVG', 'mOBP', 'mSLG', 'mOPS', 'mSBCS',
        'mIP', 'mERA', 'mWHIP', 'mKBB', 'mK9', 'mBB9', 'mHLD', 'mQS', 'mSVHLD',
        'mSV',
    )
    list_filter = ('yahoo_team__league',)


class YahooMultiLeagueTeamAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'league', 'total_win', 'total_loss', 'total_draw',
    )
    list_filter = ('league', )
    filter_horizontal = ("teams",)


class YahooRotoTeamAdmin(admin.ModelAdmin):
    list_display = (
        'team', 'total_points', 'avg', 'r', 'h',
        'hr', 'rbi', 'bb', 'k', 'obp', 'slg', 'ops', 'nsb', 'ip', 'era', 'whip',
        'kbb', 'k9', 'bb9', 'h9', 'rapp', 'sv', 'hld',
    )
    list_filter = ('team__league',)


admin.site.register(YahooTeamLeagueForecast, YahooTeamLeagueForecastAdmin)
admin.site.register(YahooMultiLeagueTeam, YahooMultiLeagueTeamAdmin)
admin.site.register(YahooTeam, YahooTeamAdmin)
admin.site.register(YahooRotoTeam, YahooRotoTeamAdmin)
