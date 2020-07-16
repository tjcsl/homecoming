from django.urls import path

from . import views
from ..auth.decorators import management_only

app_name = "events"

urlpatterns = [
    path("create/", views.create_event_view, name="create_event_page"),
    path("calendar/", views.calendar_data_view, name="calendar_source"),
    path("delete/<int:pk>", management_only(views.DeleteEventView.as_view()), name="delete"),
]
