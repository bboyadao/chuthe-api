from django.conf import settings
from django.utils.translation import gettext as _
from drf_spectacular.utils import extend_schema, OpenApiResponse

from alias.serializers import UserCreateAliasSer, UserPatchAliasSer, UserRetrieveAliasSer, UserListAliasSer, \
	ChangePathSer

TAGS = ["Alias", ]

settings.DOCS_GROUP["ALIAS"].append(TAGS)

alias_docs = {
	"change_path": extend_schema(
		request=ChangePathSer,
		responses={
			201: OpenApiResponse(response=None, description='Created with no content response'),
		},
		tags=TAGS,
		operation_id=_("Change path premium".title()),
		description=_("require: Premium member and User authenticated to create alias")
	),
	"create": extend_schema(
		request=UserCreateAliasSer,
		responses={
			201: OpenApiResponse(response=None, description='Created with no content response'),
		},
		tags=TAGS,
		operation_id=_("Create Alias".title()),
		description=_("require: User authenticated to create alias")
	),

	"retrieve": extend_schema(
		responses=UserRetrieveAliasSer,
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
		request=UserCreateAliasSer,
		responses=None,
		deprecated=True,
		auth=[],
		parameters=[],
		tags=TAGS,
		operation_id=_("Update an Alias (deprecated)".title()),
		description=_("<h3>To Update an alias please use PATCH (below) instead</h3>")
	),

	"partial_update": extend_schema(
		responses=UserPatchAliasSer,
		tags=TAGS,
		operation_id=_("Patch a field of Alias ".title()),
		description=_("All the field are optional.")
	),
}
