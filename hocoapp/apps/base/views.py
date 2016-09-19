from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

from hocoapp.decorators import login_required

import subprocess


@login_required
def index_view(request):

    events = "events"
    schedule = "schedule"
    scoreboard = "scoreboard"

    context = {
        "username": request.session["uid"],
        "name": request.session["name"],
        "events": events,
        "schedule": schedule,
        "scoreboard": scoreboard
    }
    return render(request, 'home.html', context)


def oauth_login_view(request):
    oauth_href = reverse("handle_oauth")
    context = {
        "oauth_href": oauth_href
    }
    return render(request, 'landing.html', context)
