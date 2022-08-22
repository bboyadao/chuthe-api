from django.conf import settings
from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import gettext as _

from user.serializers import UserSettingSer

TAGS = ["User Settings"]

settings.DOCS_TAG["USER"].append(TAGS)

user_docs = {

}

user_settings_docs = {
    "retrieve": extend_schema(
        tags=TAGS,
        operation_id=_("get user settings".title()),
        description="Get user settings",
        request=UserSettingSer,
        responses=UserSettingSer
    ),
    "partial_update": extend_schema(
        tags=TAGS,
        operation_id=_("update user settings".title()),
        description="Patch user settings",
        request=UserSettingSer,
        responses=UserSettingSer
    ),
}
