import boto3

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class S3Client:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def sign_url(self, object_name):
        url = self.s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': settings.MEDIAFILES_LOCATION + object_name
            },
            ExpiresIn=172800
        )
        return url

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False


    def _save_content(self, obj, content, parameters):
        # Overwritten method that call boto3 upload_fileobj
        s3 = boto3.client('s3')
        s3.upload_fileobj(content, obj.bucket_name, obj.key)
        # obj.upload_fileobj(content, ExtraArgs=put_parameters)

    def url(self, name, parameters=None, expire=None):
        if self.custom_domain:
            return S3Client().sign_url(name)


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION