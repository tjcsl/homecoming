from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse

from hocoapp.utils import is_authenticated, is_admin


def index_view(request):
    if is_authenticated(request):
        return HttpResponse("You have successfully authenticated. Your username is {}".format(request.session["uid"]))

    oauth_href = reverse("handle_oauth")

    context = {
        "oauth_href": oauth_href
    }
    return render(request, 'landing.html', context)
