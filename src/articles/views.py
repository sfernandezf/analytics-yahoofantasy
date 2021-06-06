from datetime import datetime

from django.db.models import Q
from django.views.generic import ListView, DetailView

from core.mixins.views import DomainViewMixin
from articles.models import Article


article_qs = Article.objects.filter(
    Q(is_enable=True),
    Q(start_timestamp__gt=datetime.now()) | Q(start_timestamp__isnull=True),
    Q(end_timestamp__lt=datetime.now()) | Q(end_timestamp__isnull=True)
).order_by('-created_timestamp')


class ArticleListView(ListView):
    queryset = article_qs
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    queryset = article_qs
    template_name = 'article_detail.html'


__all__ = ["ArticleListView", "ArticleDetailView"]
