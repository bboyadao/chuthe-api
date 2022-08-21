from alias.serializers import UserCreateAliasSer, UserPatchAliasSer, UserRetriveAliasSer, UserListAliasSer

from drf_spectacular.utils import extend_schema
from django.utils.translation import gettext as _
from django.conf import settings

TAGS = ["Alias"]

settings.DOCS_TAG["USER"].append(TAGS)

alias_docs = {
    "create": extend_schema(
        request=UserCreateAliasSer,
        responses=UserRetriveAliasSer,
        tags=TAGS,
        operation_id=_("Create Alias".title()),
        description=_("require: User authenticated to create alias")
    ),

    "retrieve": extend_schema(
        responses=UserRetriveAliasSer,
        tags=TAGS,
        operation_id=_("Detail alias".title()),
        description=_("Detail mai alias")
    ),

    "list": extend_schema(
        responses=UserListAliasSer(many=True),
        tags=TAGS,
        operation_id=_("Aliases".title()),
        description=_("List of alias")
    ),

    "destroy": extend_schema(

        tags=TAGS,
        operation_id=_("Delete an alias".title()),
        description=_("Delete of alias")
    ),

    "update": extend_schema(
        responses=None,
        deprecated=True,
        auth=[],
        parameters=[],
        request=None,
        tags=TAGS,
        operation_id=_("Update an Alias (deprecated)".title()),
        description=_("<h3>To Update an alias please use PATCH (below) instead</h3>")
    ),

    "partial_update": extend_schema(
        responses=UserPatchAliasSer,
        tags=TAGS,
        operation_id=_("Patch a field of Alias ".title()),
        description=_("Patch alias")
    ),

}

TAGS = ["Manage Alias"]
settings.DOCS_TAG["STAFF"].append(TAGS)
manage_alias_docs = {
    "create": extend_schema(
        # auth=[None],
        request=UserCreateAliasSer,
        responses=UserRetriveAliasSer,
        tags=TAGS,
        operation_id=_("Create An Alias".title()),
        description=_("require: User authenticated to create alias")
    ),

    "retrieve": extend_schema(
        responses=UserRetriveAliasSer,
        tags=TAGS,
        operation_id=_("View Detail alias".title()),
        description=_("Detail mai alias")
    ),

    "list": extend_schema(
        responses=UserRetriveAliasSer(many=True),
        filters=True,
        tags=TAGS,
        operation_id=_("List of Aliases".title()),
        description=_("List of alias")
    ),

    # "destroy": extend_schema(
    #
    #         tags=TAGS,
    #         operation_id=_("Delete an alias".title()),
    #         description=_("Delete of alias")
    # ),
    #
    # "update": extend_schema(
    #         responses=UserUpdateAliasSer,
    #         tags=TAGS,
    #         operation_id=_("Update an Alias ".title()),
    #         description=_("Update alias")
    #     ),
    #
    # "partial_update": extend_schema(
    #         responses=UserUpdateAliasSer,
    #         tags=TAGS,
    #         operation_id=_("Patch a field of Alias ".title()),
    #         description=_("Patch alias")
    #     ),

}
