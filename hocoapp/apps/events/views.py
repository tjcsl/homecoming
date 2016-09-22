from django.shortcuts import render, redirect
from django.urls import reverse

from hocoapp.decorators import login_required, admin_required

from .forms import CreateEventForm


@admin_required
def create_event_view(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = CreateEventForm()
    context = {"form": form}
    return render(request, "create_event_form.html", context)
