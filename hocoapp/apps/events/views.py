from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

from hocoapp.decorators import login_required, admin_required

from ..scores.models import ScoreBoard
from .forms import CreateEventForm
from .models import Event

from datetime import datetime
import json

import delorean


def unix_time_millis(dt):
    return int(delorean.Delorean(dt, timezone="UTC").epoch) * 1000


@admin_required
def create_event_view(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event_data = form.cleaned_data
            e = Event.create(event_data['name'], event_data['description'], event_data['location'], event_data['start_time'], event_data['end_time'])
            s = ScoreBoard.create(event=e)
            messages.info(request, "New event created!")
            return redirect(reverse("index"))
    else:
        form = CreateEventForm()
    context = {"form": form}
    return render(request, "create_event_form.html", context)


@login_required
def calendar_data_view(request):
    return_data = {
        "success": 1,
        "result": []
    }
    for event in Event.objects.all():
        return_data["result"].append({
            "id": event.id,
            "title": event.name,
            "start": unix_time_millis(event.start_time),
            "end": unix_time_millis(event.end_time)
        })
    return HttpResponse(json.dumps(return_data, sort_keys=True, indent=4, separators=(',', ': ')))
