

class DomainViewMixin:
    domain_path = 'domain'

    def filter_domain(self, queryset, domain_path=None):
        domain_path = domain_path or self.domain_path
        return queryset.filter(**{
            domain_path: str(self.request.META['HTTP_HOST']).split('.')[0]
        })

    def get_queryset(self):
        self.queryset = self.filter_domain(self.queryset)
        return super().get_queryset()
