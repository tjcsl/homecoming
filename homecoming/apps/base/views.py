from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..events.models import Event
from ..scores.models import ScoreBoard


@login_required
def index_view(request):
    context = {
        "events": Event.objects.all(),
        "schedule": "schedule",
        "scoreboards": ScoreBoard.objects.all().order_by("event__start_time"),
        "freshman_total": ScoreBoard.objects.aggregate(Sum("freshman_score"))["freshman_score__sum"],
        "sophomore_total": ScoreBoard.objects.aggregate(Sum("sophomore_score"))["sophomore_score__sum"],
        "junior_total": ScoreBoard.objects.aggregate(Sum("junior_score"))["junior_score__sum"],
        "senior_total": ScoreBoard.objects.aggregate(Sum("senior_score"))["senior_score__sum"],
    }

    for key in context:
        if key.endswith("total") and not context[key]:
            context[key] = 0
    return render(request, "home.html", context)


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
