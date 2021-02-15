from typing import Dict, List

DEBUG = True
SECRET_KEY = "y_xy)s%b_0h=#=y#3le5wfk!iy_+w#3#2j_&g@k^u-^qbrhxl2"

AUTHENTICATION_BACKENDS: List[str] = ["homecoming.apps.auth.oauth.IonOauth2"]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS: List[Dict] = []
    AUTHENTICATION_BACKENDS += "django.contrib.auth.backends.ModelBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "homecoming",
        "USER": "homecoming",
        "PASSWORD": "pwd",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

SENTRY_DSN = ""

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_ION_KEY = ""
SOCIAL_AUTH_ION_SECRET = ""
