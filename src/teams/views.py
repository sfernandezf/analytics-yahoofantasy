from django.shortcuts import render
from django.views.generic import ListView

from teams.models import YahooTeam


class TeamViews(ListView):
    queryset = YahooTeam.objects.all().order_by('-total_win')
    template_name = "yahooteamstats_list.html"

    def get_queryset(self):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        self.queryset = self.queryset.filter(
            league__domain=subdomain,
            league__is_active=True,
        )
        return super(TeamViews, self).get_queryset()

