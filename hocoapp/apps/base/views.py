from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Sum

from hocoapp.decorators import login_required
from hocoapp.apps.events.models import Event
from hocoapp.apps.scores.models import ScoreBoard

import subprocess


@login_required
def index_view(request):

    events = Event.objects.all().order_by("start_time")
    schedule = "schedule"
    scoreboards = ScoreBoard.objects.all().order_by("event__start_time")

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

def api_view(request):
    context = {
        "freshman_total": ScoreBoard.objects.aggregate(Sum("freshman_score"))["freshman_score__sum"],
        "sophomore_total": ScoreBoard.objects.aggregate(Sum("sophomore_score"))["sophomore_score__sum"],
        "junior_total": ScoreBoard.objects.aggregate(Sum("junior_score"))["junior_score__sum"],
        "senior_total": ScoreBoard.objects.aggregate(Sum("senior_score"))["senior_score__sum"],
    }
    resp = JsonResponse(context)
    resp["Access-Control-Allow-Origin"] = "*"
    resp["Access-Control-Allow-Headers"] = "x-requested-with"
    return resp
