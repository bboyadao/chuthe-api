
from alias.serializers import UserCreateAliasSer, UserRetrieveAliasSer

from drf_spectacular.utils import extend_schema
from django.utils.translation import gettext as _
from django.conf import settings

#  todo: not yet impl
TAGS = ["Manage Alias"]
settings.DOCS_TAG["STAFF"].append(TAGS)
manage_alias_docs = {
    "create": extend_schema(
        # auth=[None],
        request=UserCreateAliasSer,
        responses=UserRetrieveAliasSer,
        tags=TAGS,
        operation_id=_("Create An Alias".title()),
        description=_("require: User authenticated to create alias")
    ),

    "retrieve": extend_schema(
        responses=UserRetrieveAliasSer,
        tags=TAGS,
        operation_id=_("View Detail alias".title()),
        description=_("Detail mai alias")
    ),

    "list": extend_schema(
        responses=UserRetrieveAliasSer(many=True),
        filters=True,
        tags=TAGS,
        operation_id=_("List of Aliases".title()),
        description=_("List of alias")
    ),
}
