import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "this is a secrety key"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "homecoming.tjhsst.edu"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "homecoming.apps",
    "homecoming.apps.auth.apps.AuthConfig",
    "homecoming.apps.base.apps.BaseConfig",
    "homecoming.apps.scores.apps.ScoresConfig",
    "homecoming.apps.events.apps.EventsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "homecoming.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "homecoming.apps.context_processors.base_context",
            ]
        },
    }
]
WSGI_APPLICATION = "homecoming.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
AUTH_USER_MODEL = "authentication.User"

AUTHENTICATION_BACKENDS = ["homecoming.apps.auth.oauth.IonOauth2"]

SOCIAL_AUTH_USER_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "id",
    "is_student",
    "is_teacher",
    "is_staff",
    "is_superuser",
]
SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
)
SOCIAL_AUTH_ALWAYS_ASSOCIATE = True
SOCIAL_AUTH_LOGIN_ERROR_URL = reverse_lazy("auth:index")
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True


LOGIN_URL = reverse_lazy("auth:login")
LOGIN_REDIRECT_URL = reverse_lazy("base:index")
LOGOUT_REDIRECT_URL = reverse_lazy("auth:login")

SESSION_SAVE_EVERY_REQUEST = True


LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "America/New_York"


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "serve/")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)


HOMECOMING_YEAR = 2022
HOMECOMING_DISPLAY_YEAR = 2022  # used if homecoming occurs in the spring

try:
    from .secret import *  # noqa  # pylint: disable=unused-import
except ImportError:
    DEBUG = True
    SENTRY_DSN = ""

if not DEBUG:
    sentry_sdk.init(
        SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
    )
