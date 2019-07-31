from .utils import is_authenticated, is_admin


def auth_processor(request):
    return {"is_admin": is_admin(request), "is_authenticated": is_authenticated(request)}
