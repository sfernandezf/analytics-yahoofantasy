from django.views.generic import ListView

from leagues.models import YahooLeague


class ResultViews(ListView):
    queryset = YahooLeague.objects.all()
    template_name = "results_list.html"

    def get_queryset(self):
        subdomain = str(self.request.META['HTTP_HOST']).split('.')[0]
        self.queryset = self.queryset.filter(
            domain=subdomain,
            is_active=True,
        )
        return super(ResultViews, self).get_queryset()

