import os

from django.db.models import FileField, ImageField

__all__ = ["S3CustomFileField", "S3CustomImageField"]


class S3CustomFileField(FileField):
    def __init__(
        self,
        verbose_name=None,
        name=None,
        upload_to="",
        storage=None,
        is_name_auto=True,
        **kwargs,
    ):
        super().__init__(
            verbose_name=verbose_name,
            name=name,
            upload_to=upload_to,
            storage=storage,
            **kwargs,
        )
        self.is_name_auto = is_name_auto
        self.format = format

    def get_name(self, instance, filename):
        if self.is_name_auto is False or not hasattr(instance, "id"):
            return filename
        _, file_extension = os.path.splitext(filename)
        return "/".join((str(instance.id), self.attname + file_extension))

    def generate_filename(self, instance, filename):
        filename = self.get_name(instance, filename)
        return super().generate_filename(instance, filename)


class S3CustomImageField(ImageField, S3CustomFileField):
    pass
