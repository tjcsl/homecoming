from django.shortcuts import render

def index_view(request):
    if request.user.is_authenticated():
        # Do something
        pass

    context = {}
    return render(request, 'landing.html', context)
