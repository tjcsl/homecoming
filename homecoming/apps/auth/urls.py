from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "class_group/edit/<int:class_group_id>/",
        views.edit_class_group_view,
        name="edit_class_group",
    ),
]
