from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

from hocoapp.decorators import login_required
from hocoapp.apps.events.models import Event

import subprocess


@login_required
def index_view(request):

    events = Event.objects.all()
    schedule = "schedule"
    scoreboard = "scoreboard"

    context = {
        "events": events,
        "schedule": schedule,
        "scoreboard": scoreboard
    }
    return render(request, 'home.html', context)
