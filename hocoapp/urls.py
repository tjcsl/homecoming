"""hocoapp URL Configuration
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .apps.base import views as base_views
from .apps.users import views as user_views
from .apps.scores import views as score_views
from .apps.events import views as event_views

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", base_views.index_view, name="index"),
    url(r"^api/$", base_views.api_view, name="api"),
    url(r"^oauth/$", user_views.handle_oauth, name="handle_oauth"),
    url(r"^logout/$", auth_views.logout, {"next_page": "/"}, name="logout"),
    url(r"^events/create/$", event_views.create_event_view, name="create_event_page"),
    url(r"^events/calendar/$", event_views.calendar_data_view, name="calendar_source"),
    url(r"^scores/edit/(?P<event_id>\d+)/$", score_views.edit_scores_view, name="edit_scores"),
]
