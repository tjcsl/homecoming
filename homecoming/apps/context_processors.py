from typing import Any, Dict

from django.conf import settings
from django.http import HttpRequest


def base_context(request: HttpRequest) -> Dict[str, Any]:
    return {
        "homecoming_year": settings.HOMECOMING_YEAR,
    }
