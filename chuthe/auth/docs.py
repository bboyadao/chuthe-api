from drf_spectacular.utils import extend_schema
from django.utils.translation import gettext as _

from django.conf import settings

from chuthe.auth.serializers import ShitResponseSerialiser, LogoutRequestSerialiser

TAG = "Auth"
settings.DOCS_TAG["PUBLIC"].append(TAG)
PUBLIC_TAGS = [TAG]
login_docs = {
    "post": extend_schema(
        tags=[TAG],
        operation_id=_("Login".title()),
        description="Login Dess"
    ),
}

reset_password_confirm_docs = {
    "post": extend_schema(
        responses=ShitResponseSerialiser,
        tags=[TAG],
        operation_id=_("reset password confirm".title()),
        description=""
    ),
}

reset_password_docs = {
    "post": extend_schema(
        responses=ShitResponseSerialiser,
        tags=[TAG],
        operation_id=_("reset password".title()),
        description=""
    ),
}
TAG = "Account"
settings.DOCS_TAG["USER"].append(TAG)
logout_docs = {
    "post": extend_schema(
        tags=[TAG],
        request=LogoutRequestSerialiser,
        responses=ShitResponseSerialiser,
        operation_id=_("Log out (post)".title()),
        description="Logout (Recommend)"
    ),
    "get": extend_schema(
        tags=[TAG],
        responses=ShitResponseSerialiser,
        operation_id=_("Log out (get)".title()),
        description="Not recommend!"
    )
}

change_password_docs = {
    "post": extend_schema(
        responses=ShitResponseSerialiser,
        tags=[TAG],
        operation_id=_("change password".title()),
        description=""
    ),
}

user_detail_docs = {
    "get": extend_schema(
        tags=[TAG],
        operation_id=_("user detail".title()),
        description=""
    ),
}