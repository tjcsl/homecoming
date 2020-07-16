from datetime import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..auth.decorators import management_only
from ..scores.models import ScoreBoard
from .forms import CreateEventForm
from .models import Event


def unix_time_millis(dt):
    return int(round(datetime.timestamp(dt)*1000))


@management_only
def create_event_view(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event_data = form.cleaned_data
            e = Event.create(event_data["name"], event_data["description"], event_data["location"], event_data["start_time"], event_data["end_time"])
            ScoreBoard.create(event=e)
            messages.info(request, "New event created!")
            return redirect(reverse("base:index"))
    else:
        form = CreateEventForm()
    context = {"form": form}
    return render(request, "events/create_event_form.html", context)


@login_required
def calendar_data_view(request):
    data = {"success": 1, "result": []}
    for event in Event.objects.all():
        data["result"].append(
            {"id": event.id, "title": event.name, "start": unix_time_millis(event.start_time), "end": unix_time_millis(event.end_time)}
        )
    resp = JsonResponse(data)

    resp["Access-Control-Allow-Origin"] = "*"
    resp["Access-Control-Allow-Headers"] = "x-requested-with"

    return resp
