from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError

import json

# Create your views here.


def handle_oauth(request):
    oauth = OAuth2Session(
        settings.CLIENT_ID, redirect_uri=settings.REDIRECT_URI, scope=["read"])
    if 'error' in request.GET:
        context = {
            "message": request.GET["error"],
            "oauth_href": reverse("handle_oauth")
        }
        return render(request, "landing.html", context)
    if 'code' not in request.GET:
        authorization_url, state = oauth.authorization_url(
            "https://ion.tjhsst.edu/oauth/authorize/")
        return redirect(authorization_url)
    try:
        token = oauth.fetch_token("https://ion.tjhsst.edu/oauth/token/",
                                  code=request.GET['code'], client_secret=settings.CLIENT_SECRET)
        profile = oauth.get("https://ion.tjhsst.edu/api/profile")
        user_data = json.loads(profile.content.decode())
        request.session["uid"] = user_data["ion_username"]
        return redirect(reverse("index"))
    except InvalidGrantError:
        return redirect(reverse("handle_oauth"))
