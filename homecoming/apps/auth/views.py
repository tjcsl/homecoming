from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "auth/login.html")
