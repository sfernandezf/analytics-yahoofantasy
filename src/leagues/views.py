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

    def get_context_data(self, *args, object_list=None, **kwargs):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        multi_leages = []
        for object in self.queryset:
            multi_leages.append(object)
        for object in YahooMultiYearLeague.objects.filter(domain=subdomain, is_active=True):
            multi_leages.append(object)
        context['multi_leages'] = multi_leages
        return context

