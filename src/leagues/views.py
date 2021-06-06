from django.shortcuts import render
from django.views.generic import ListView

from core.mixins.views import DomainViewMixin
from leagues.models import YahooLeague, YahooMultiYearLeague


class LeagueViews(DomainViewMixin, ListView):
    queryset = YahooLeague.objects.filter(
        is_active=True
    ).order_by('created_timestamp')
    template_name = "yahooleague_list.html"
