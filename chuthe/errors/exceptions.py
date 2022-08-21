from django.http import JsonResponse
from rest_framework import status
from django.utils.translation import gettext as _

import logging

logger = logging.getLogger(__name__)

def chuthe_server_5xx(request, *args, **kwargs):  # noqa
    data = {
        'error': _('Unknown error'),
        "request_id": request.extra["request_id"]
    }
    logger.critical("critical", extra=request.extra, exc_info=True)
    return JsonResponse(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
