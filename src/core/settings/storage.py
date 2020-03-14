# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
import os


STATIC_URL = "/static/"
if ENVIRONMENT == "local":
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
