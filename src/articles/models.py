from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel
from core.mixins.fields import S3CustomImageField


class Article(BaseModel):
    def __str__(self):
        return self.title

    title = models.CharField(_("Title"), max_length=1024)
    description = models.TextField(_("Description"), null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(_("Content"))
    author = models.ForeignKey(
        to='users.User', verbose_name=_("Autor"), on_delete=models.SET_NULL,
        null=True, blank=True
    )
    is_enable = models.BooleanField(_("Is Enabled"), default=True)
    start_timestamp = models.DateTimeField(
        _("Start Datetime"), null=True, blank=True, default=None
    )
    end_timestamp = models.DateTimeField(
        _("End Datetime"), null=True, blank=True, default=None
    )
    main_image = S3CustomImageField(
        upload_to="articles", max_length=1024
    )

    @property
    def description_repr(self):
        return (
            self.description if self.description
            else f"{self.content[:256]} ..."
        )
