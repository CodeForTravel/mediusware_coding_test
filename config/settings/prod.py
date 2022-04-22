from .base import *

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = env.str("EMAIL_HOST")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env.str("EMAIL_PORT")
EMAIL_NOREPLY = "mdfaisalnstu@gmail.com"

CORS_ORIGIN_WHITELIST = []

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = []
