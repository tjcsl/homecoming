from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

from hocoapp.decorators import login_required
from hocoapp.apps.events.models import Event
from hocoapp.apps.scores.models import ScoreBoard

import subprocess


@login_required
def index_view(request):

    events = Event.objects.all()
    schedule = "schedule"
    scoreboards = ScoreBoard.objects.all()

    context = {
        "events": events,
        "schedule": schedule,
        "scoreboards": scoreboards
    }
    return render(request, 'home.html', context)
