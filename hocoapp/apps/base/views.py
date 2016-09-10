from django.shortcuts import render
from django.conf import settings

def index_view(request):
    if request.user.is_authenticated():
        # Do something
        pass

    oauth_state = ""

    oauth_href = settings.OAUTH_PROVIDER + \
                 "?response_type=code" + \
                 "&client_id={}".format(settings.OAUTH_CLIENT_ID) + \
                 "&redirect_uri={}".format(settings.OAUTH_REDIRECT_URI) + \
                 "&scope=read&state={}".format(oauth_state)

    context = {
        "oauth_href": oauth_href
    }
    return render(request, 'landing.html', context)
