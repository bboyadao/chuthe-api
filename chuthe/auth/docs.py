from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import gettext as _

from django.conf import settings

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
        operation_id=_("Log out".title()),
        description="Login Dess"
    ),
}
PUBLIC_TAGS = [TAG]
