from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

from hocoapp.utils import is_authenticated, is_admin

import subprocess


def index_view(request):
    if not is_authenticated(request):
        oauth_href = reverse("handle_oauth")

        context = {
            "oauth_href": oauth_href
        }
        return render(request, 'landing.html', context)

    events = "events"
    schedule = "schedule"
    scoreboard = "scoreboard"

    context = {
        "username": request.session["uid"],
        "events": events,
        "schedule": schedule,
        "scoreboard": scoreboard
    }
    return render(request, 'home.html', context)
