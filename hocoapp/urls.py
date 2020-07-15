from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("", include("hocoapp.apps.auth.urls", namespace="auth")),
    path("", include("hocoapp.apps.base.urls", namespace="base")),
    path("events/", include("hocoapp.apps.events.urls", namespace="events")),
    path("scores/", include("hocoapp.apps.scores.urls", namespace="scores")),
]
