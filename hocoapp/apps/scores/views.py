from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import ScoreBoard
from .forms import EditScoresForm


def edit_scores_view(request, event_id):
    scoreboard = get_object_or_404(ScoreBoard, event_id=event_id)
    if request.method == "POST":
        form = EditScoresForm(request.POST, instance=scoreboard)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = EditScoresForm(instance=scoreboard)
    context = {"form": form, "scoreboard": scoreboard}
    return render(request, "edit_scores_page.html", context)
