from django.shortcuts import render
from django.views.generic import ListView

from leagues.models import YahooLeague, YahooMultiYearLeague


class LeagueViews(ListView):
    queryset = YahooLeague.objects.all()
    template_name = "yahooleague_list.html"

    def get_queryset(self):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        self.queryset = self.queryset.filter(
            domain=subdomain,
            is_active=True,
        )
        return super(LeagueViews, self).get_queryset()

