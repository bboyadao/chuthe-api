import uuid
from django.conf import settings
from django.utils import timezone

from rest_framework.request import Request
logger = settings.LOGGER


class ChutheIOMiddleware:
    extra = dict()
    reach_time = 0.2

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_or_create_request_id(request):
        _id = request.META.get("cf-request-id") or request.META.get("X-Amzn-Trace-Id") or uuid.uuid4().__str__()
        return _id

    def __call__(self, request: Request) -> None:
        request.reques_id = self.get_or_create_request_id(request)
        self.extra["request_id"] = request.reques_id

        t_start = timezone.now()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        self.extra['ip'] = ip

        self.extra['user'] = request.user.__str__()
        self.extra['uri'] = request.build_absolute_uri()
        self.extra['body'] = request.body
        self.extra['request_id'] = request.META.get("cf-request-id", uuid.uuid4().__str__())

        request.extra = self.extra
        response = self.get_response(request)
        delta_time = (timezone.now() - t_start).total_seconds()

        if delta_time > self.reach_time:
            func_path = request.resolver_match._func_path  # noqa
            self.extra["viewName"] = request.resolver_match.view_name
            self.extra["viewPath"] = func_path
            logger.warn(f"View name`{request.resolver_match.view_name}` at: `{func_path}` exec "
                        f"limit of time", extra=self.extra)
        return response
