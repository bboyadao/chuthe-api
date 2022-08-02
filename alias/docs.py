from alias.serializers import UserCreateAliasSer, UserUpdateAliasSer, UserRetriveAliasSer

from drf_spectacular.utils import extend_schema
from django.utils.translation import gettext as _

from django.db import models


class ROLE(models.TextChoices):
    ADMIN = _("ADMINSTRATOR"), _("ADMINSTRATOR").title()
    STAFF = _("STAFF"), _("STAFF").title()
    PUBLIC = _("PUBLIC"), _("PUBLIC").title()
    USER = _("USER"), _("USER").title()


TAGS = [ROLE.USER]
alias_docs = {
    "create": extend_schema(
        # auth=[None],
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
        responses=UserRetriveAliasSer(many=True),
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
            responses=UserUpdateAliasSer,
            tags=TAGS,
            operation_id=_("Update an Alias ".title()),
            description=_("Update alias")
        ),

    "partial_update": extend_schema(
            responses=UserUpdateAliasSer,
            tags=TAGS,
            operation_id=_("Patch a field of Alias ".title()),
            description=_("Patch alias")
        ),


}

