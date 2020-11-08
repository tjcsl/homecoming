from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

from ..auth.decorators import management_only
from ..scores.models import ScoreBoard
from .forms import CreateEventForm
from .models import Event


def unix_time_millis(dt):
    return int(round(datetime.timestamp(dt) * 1000))


@management_only
def create_event_view(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            e = form.save()
            ScoreBoard.objects.create(event=e)
            messages.info(request, "New event created!")
            return redirect(reverse("base:index"))
        else:
            for errors in form.errors.get_json_data().values():
                for error in errors:
                    messages.error(request, error["message"])
    return render(request, "events/create_event_form.html", {"form": CreateEventForm()})


class DeleteEventView(DeleteView):
    model = Event
    template_name = "events/delete.html"
    success_url = reverse_lazy("base:index")
    success_message = "Deleted Event Successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_url)
        return super().delete(request, *args, **kwargs)


@login_required
def calendar_data_view(request):
    data = {"success": 1, "result": []}
    for event in Event.objects.all():
        data["result"].append(
            {
                "id": event.id,
                "title": event.name,
                "start": unix_time_millis(event.start_time),
                "end": unix_time_millis(event.end_time),
            }
        )
    resp = JsonResponse(data)

    resp["Access-Control-Allow-Origin"] = "*"
    resp["Access-Control-Allow-Headers"] = "x-requested-with"

    return resp
