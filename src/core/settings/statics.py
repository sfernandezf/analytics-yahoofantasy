import os


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)


# Statics File and Media Configuration
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
if ENVIRONMENT == 'local':
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIAFILES_LOCATION='media'
    STATICFILES_LOCATION='static'

else:
    STATICFILES_STORAGE = 'core.storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'core.storages.MediaStorage'

    # s3 Configuration
    AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', default='us-east-1')
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN') # CloudFront
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    MEDIAFILES_LOCATION = env('MEDIAFILES_LOCATION')
    STATICFILES_LOCATION = env('STATICFILES_LOCATION')
    AWS_DEFAULT_ACL = None


