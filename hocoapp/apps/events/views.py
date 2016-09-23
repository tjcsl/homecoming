from django.shortcuts import render, redirect
from django.urls import reverse

from hocoapp.decorators import login_required, admin_required

from ..scores.models import ScoreBoard
from .forms import CreateEventForm
from .models import Event


@admin_required
def create_event_view(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event_data = form.cleaned_data
            e = Event.create(event_data['name'], event_data['description'], event_data['time'])
            s = ScoreBoard.create(event=e)
            return redirect(reverse("index"))
    else:
        form = CreateEventForm()
    context = {"form": form}
    return render(request, "create_event_form.html", context)
