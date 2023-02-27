from django.conf import settings
from django.utils.translation import gettext as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

from alias.serializers import LinkSer

TAGS = ["Social"]
settings.DOCS_TAG["ALIAS"].append(TAGS)

social_docs = {
	"create": extend_schema(
		parameters=[
			OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)
		],

		request=LinkSer,
		responses={
			201: OpenApiResponse(response=None, description='Created with no content response'),
		},
		tags=TAGS,
		operation_id=_("Create Social".title()),
		description=_("require: User authenticated to create alias")
	),

	"list": extend_schema(
		parameters=[
			OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)
		],
		responses=LinkSer(many=True),
		tags=TAGS,
		operation_id=_("Socials".title()),
		description=_("List of links")
	),

	"destroy": extend_schema(
		parameters=[
			OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)
		],
		tags=TAGS,
		operation_id=_("Delete a Social".title()),
		description=_("Delete of link")
	),

	"partial_update": extend_schema(
		parameters=[
			OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)
		],
		responses=LinkSer,
		tags=TAGS,
		operation_id=_("Patch a field of Social ".title()),
		description=_("All the field are optional.")
	),
}
