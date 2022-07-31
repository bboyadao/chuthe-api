from alias.serializers import UserCreateAliasSer, UserUpdateAliasSer, UserRetriveAliasSer

from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import gettext as _


TAG = "Alias (User)"

alias_docs = {
    "create": extend_schema(
        request=UserCreateAliasSer,
        responses=UserRetriveAliasSer,
        tags=[TAG],
        operation_id=_("Create Alias".title()),
        description="require: User authenticated to create alias"
    ),

    "retrieve": extend_schema(
        responses=UserRetriveAliasSer,
        tags=[TAG],
        operation_id=_("Detail alias".title()),
        description="Detail mai alias"
    ),

    "list": extend_schema(
        responses=UserRetriveAliasSer(many=True),
        tags=[TAG],
        operation_id=_("Aliases".title()),
        description="List of alias"
    ),

    "destroy": extend_schema(

            tags=[TAG],
            operation_id=_("Delete an alias".title()),
            description="Delete of alias"
    ),

    "update": extend_schema(
            responses=UserUpdateAliasSer,
            tags=[TAG],
            operation_id=_("Update an Alias ".title()),
            description="Update alias"
        ),

    "partial_update": extend_schema(
            responses=UserUpdateAliasSer,
            tags=[TAG],
            operation_id=_("Patch a field of Alias ".title()),
            description="Patch alias"
        ),


}

