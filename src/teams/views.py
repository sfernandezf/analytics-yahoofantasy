from django.shortcuts import render
from django.views.generic import ListView

from core.mixins.views import DomainViewMixin

from teams.models import YahooTeam, YahooMultiLeagueTeam, YahooRotoTeam


class TeamViews(DomainViewMixin, ListView):
    domain_path = 'league__domain'
    queryset = YahooTeam.objects.filter(
        league__is_active=True
    ).order_by('-w_pct')
    template_name = "yahooteamstats_list.html"


class RotoTeamViews(DomainViewMixin, ListView):
    domain_path = 'league__domain'
    queryset = YahooRotoTeam.objects.filter(
        league__is_active=True
    ).order_by('-total_points')
    template_name = "yahoorototeam_list.html"
