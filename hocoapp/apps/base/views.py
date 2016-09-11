from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse

from hocoapp.utils import is_authenticated, is_admin


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

