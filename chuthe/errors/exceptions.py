from rest_framework.views import exception_handler
from django.conf import settings
from user.models import User
from django.utils.translation import gettext as _
from rest_framework.request import Request
logger = settings.LOGGER


def chuthe_exception_handler(_exception, context):
    response = exception_handler(_exception, context)
    request: Request = context["request"]
    user: User = request.user
    msg = "Exception: "
    match user.is_authenticated:
        case False:
            msg += _(f"{_exception.default_detail} | Guest")
        case True:
            msg += _(f"{_exception.default_detail} | User {user.__str__()}")

    if _exception.status_code >= 500:
        logger.error(msg, extra=request.extra, stack_info=True)
    elif _exception.status_code < 500:
        # TODO: add more detail and impl to user activity
        logger.warn(msg, extra=request.extra)
    return response
