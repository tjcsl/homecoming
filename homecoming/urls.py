from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("", include("homecoming.apps.auth.urls", namespace="auth")),
    path("", include("homecoming.apps.base.urls", namespace="base")),
    path("events/", include("homecoming.apps.events.urls", namespace="events")),
    path("scores/", include("homecoming.apps.scores.urls", namespace="scores")),
]
