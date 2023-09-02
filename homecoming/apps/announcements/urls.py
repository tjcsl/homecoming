from django.urls import path

from ..auth.decorators import management_or_class_group_admin_only
from . import views

app_name = "announcements"

urlpatterns = [
    path("create/", views.create_announcement_view, name="create_announcement_page"),
    path(
        "edit/<int:announcement_id>/",
        views.edit_announcement_view,
        name="edit_announcement",
    ),
    path(
        "delete/<int:pk>",
        management_or_class_group_admin_only(views.DeleteAnnouncementView.as_view()),
        name="delete",
    ),
]
