from django.views.generic import ListView

from core.mixins.views import DomainViewMixin
from leagues.models import YahooLeague, YahooMultiYearLeague


class ResultViews(DomainViewMixin, ListView):
    queryset = YahooLeague.objects.filter(
        is_active=True
    ).order_by('created_timestamp')
    template_name = "results_list.html"
