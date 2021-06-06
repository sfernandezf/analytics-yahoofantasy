from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_timestamp', 'is_enable')
    list_filter = (
        'is_enable',
    )


admin.site.register(Article, ArticleAdmin)

