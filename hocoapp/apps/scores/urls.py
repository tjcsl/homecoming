from django.urls import path

from . import views

app_name = "scores"

urlpatterns = [
    path("edit/<int:event_id>/", views.edit_scores_view, name="edit_scores")
]

