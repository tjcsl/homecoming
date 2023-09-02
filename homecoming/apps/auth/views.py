from django import http
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

from .decorators import management_or_class_group_admin_only
from .models import ClassGroup
from .forms import ClassGroupForm


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "auth/login.html")


@management_or_class_group_admin_only
def edit_class_group_view(request: HttpRequest, class_group_id: int) -> HttpResponse:
    class_group = get_object_or_404(ClassGroup, id=class_group_id)

    if (
        request.user.is_class_group_admin
        and not request.user.has_management_permission
        and request.user.class_group != class_group
    ):
        raise http.Http404

    if request.method == "POST":
        form = ClassGroupForm(data=request.POST, instance=class_group)
        if form.is_valid():
            form.save()
            messages.info(request, "Announcement edited!")
            return redirect(reverse("base:index"))
    else:
        form = ClassGroupForm(instance=class_group)

    return render(request, "auth/class_group_form.html", {"form": form, "id": class_group_id})
