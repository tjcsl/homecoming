from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from hocoapp.utils import is_authenticated, is_admin

import subprocess


def index_view(request):
    if not is_authenticated(request):
        oauth_href = reverse("handle_oauth")

        context = {
            "oauth_href": oauth_href
        }
        return render(request, 'landing.html', context)

    context = {
        "username": request.session["uid"]
    }
    return render(request, 'home.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def git_webhook(request):
    command = ["git", "pull"]
    subprocess.check_output(command).decode()
    return HttpResponse("Successful")
