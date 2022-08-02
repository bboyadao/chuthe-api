from drf_spectacular.utils import extend_schema
from django.utils.translation import gettext as _

from django.conf import settings

from chuthe.auth.serializers import LogoutResponseSerialiser, LogoutRequestSerialiser

TAG = "Auth"

settings.DOCS_TAG["PUBLIC"].append(TAG)

login_docs = {
    "post": extend_schema(
        tags=[TAG],
        operation_id=_("Login".title()),
        description="Login Dess"
    ),
}
logout_docs = {
    "post": extend_schema(
        tags=[TAG],
        request=LogoutRequestSerialiser,
        responses=LogoutResponseSerialiser,
        operation_id=_("Log out (post)".title()),
        description="Login Dess"
    ),
    "get": extend_schema(
        tags=[TAG],
        responses=LogoutResponseSerialiser,
        operation_id=_("Log out (get)".title()),
        description="Login Dess"
    )
}
PUBLIC_TAGS = [TAG]
