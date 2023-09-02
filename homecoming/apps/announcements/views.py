import datetime

from django import http
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

from ..auth.decorators import management_only, management_or_class_group_admin_only
from ..scores.models import ScoreBoard
from .forms import AnnouncementForm
from .models import Announcement


def unix_time_millis(datetime_obj: datetime.datetime) -> int:
    """
    Returns the number of milliseconds since the Unix epoch.

    Args:
        datetime_obj: a datetime.datetime object to calculate from

    Returns:
        an integer
    """
    return int(round(datetime.datetime.timestamp(datetime_obj) * 1000))


@management_or_class_group_admin_only
def create_announcement_view(request: HttpRequest) -> HttpResponse:
    """
    View to create an event.

    Args:
        request: HttpRequest

    Returns:
        HttpResponse
    """
    # no user validation needed because AnnouncementForm handles it

    if request.method == "POST":
        form = AnnouncementForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "New announcement created!")
            return redirect(reverse("base:index"))
        else:
            for errors in form.errors.get_json_data().values():
                for error in errors:
                    messages.error(request, error["message"])
    else:
        form = AnnouncementForm(user=request.user)
    return render(
        request,
        "announcements/announcement_form.html",
        {"form": form},
    )


@management_or_class_group_admin_only
def edit_announcement_view(request: HttpRequest, announcement_id: int) -> HttpResponse:
    """
    The view to edit an announcement

    Args:
        request: HttpRequest
        announcement_id: the ID of the announcement to edit

    Returns:
        HttpResponse
    """
    announcement = get_object_or_404(Announcement, id=announcement_id)

    # a class group admin from a different class group cannot access the url to read the
    # announcement or move it to their own class group
    if (
        request.user.is_class_group_admin
        and not request.user.has_management_permission
        and request.user.class_group != announcement.class_group
    ):
        raise http.Http404

    if request.method == "POST":
        form = AnnouncementForm(data=request.POST, instance=announcement, user=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Announcement edited!")
            return redirect(reverse("base:index"))
    else:
        form = AnnouncementForm(instance=announcement, user=request.user)

    return render(
        request, "announcements/announcement_form.html", {"form": form, "id": announcement_id}
    )


class DeleteAnnouncementView(DeleteView):
    model = Announcement
    template_name = "announcements/delete.html"
    success_url = reverse_lazy("base:index")
    success_message = "Deleted Announcement Successfully"

    def delete(self, request, *args, **kwargs):
        if request.user.class_group != self.get_object().class_group:
            raise http.Http404
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)
