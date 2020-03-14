import datetime
from datetime import timedelta


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Django Change UserModel
AUTH_USER_MODEL = "users.User"


# django-rest-auth Configuration
# https://django-rest-auth.readthedocs.io/en/latest/configuration.html
INSTALLED_APPS += [
    "rest_framework.authtoken",
    "rest_auth",
]

REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "auth.serializers.LoginSerializer",
    "USER_DETAILS_SERIALIZER": "users.serializers.UserSerializer",
    "JWT_SERIALIZER": "auth.serializers.JWTSerializer"
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "auth.serializers.RegisterSerializer"
}
REST_SESSION_LOGIN = False
REST_USE_JWT = True
JWT_AUTH_COOKIE = None


# allauth Configuration
# https://django-allauth.readthedocs.io/en/latest/configuration.html
INSTALLED_APPS += [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "rest_auth.registration",
]

SITE_ID = 1
ACCOUNT_ADAPTER = "auth.adapters.AccountAdapter"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_DISPLAY = "user.email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# djangorestframework-simplejwt Configuration
#https://github.com/davesque/django-rest-framework-simplejwt
INSTALLED_APPS += [
    "rest_framework_simplejwt.token_blacklist"
]
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        hours=env('ACCESS_TOKEN_LIFETIME', default=2)),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        hours=env('REFRESH_TOKEN_LIFETIME', default=12)),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}



AUTH_ALLOW_REGISTRATION = False