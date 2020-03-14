EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = "yes"
DEFAULT_FROM_EMAIL = env("EMAIL_FROM", default="no-reply@lighthousetech.io")
DEFAULT_REPLY_TO = env("EMAIL_REPLY_TO", default="support@lighthousetech.io")
EMAIL_HOST_USER = env("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
