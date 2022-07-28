from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import gettext as _


TAG = "Auth"
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