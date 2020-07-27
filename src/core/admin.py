from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django_json_widget.widgets import JSONEditorWidget


class JSONFieldWidgetAdminMixin:
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }