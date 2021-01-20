from django.shortcuts import render
from django.views.generic import ListView

from teams.models import YahooTeam, YahooMultiLeagueTeam


class TeamViews(ListView):
    queryset = YahooTeam.objects.all().order_by('-w_pct')
    template_name = "yahooteamstats_list.html"

    def get_queryset(self):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        self.queryset = self.queryset.filter(
            league__domain=subdomain,
            league__is_active=True,
        )
        return super(TeamViews, self).get_queryset()

    def get_context_data(self, *args, object_list=None, **kwargs):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        multi_teams = []
        for object in self.queryset:
            multi_teams.append(object)
        for object in YahooMultiLeagueTeam.objects.filter(
                league__domain=subdomain, league__is_active=True).order_by('-w_pct'):
            multi_teams.append(object)
        context['multi_teams'] = multi_teams
        return context

