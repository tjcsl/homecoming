from functools import wraps

from hocoapp.utils import is_authenticated, is_admin

from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if is_authenticated(args[0]):
            return f(*args, **kwargs)
        return redirect(reverse("handle_oauth"))

    return wrapper


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if is_admin(args[0]):
            return f(*args, **kwargs)
        messages.error(args[0], "You must be an admin to access this page.")
        return redirect(reverse("index"))

    return wrapper
