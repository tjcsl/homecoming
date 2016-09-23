from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

from django.db.models import Sum

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
        "scoreboards": scoreboards,
        "freshman_total": ScoreBoard.objects.aggregate(Sum("freshman_score"))["freshman_score__sum"],
        "sophomore_total": ScoreBoard.objects.aggregate(Sum("sophomore_score"))["sophomore_score__sum"],
        "junior_total": ScoreBoard.objects.aggregate(Sum("junior_score"))["junior_score__sum"],
        "senior_total": ScoreBoard.objects.aggregate(Sum("senior_score"))["senior_score__sum"],
    }
    return render(request, 'home.html', context)
