from allauth.socialaccount.providers import registry
from django.conf import settings
from django.utils.translation import gettext as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view, OpenApiParameter, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from helpers import vn_banks, wallet_vn

TAGS = ["Const", ]

settings.DOCS_TAG["USER"].append(TAGS)

docs_ = {
	"retrieve": extend_schema(
			parameters=[
				OpenApiParameter(
						name='name',
						type=OpenApiTypes.STR,
						enum=[
							"providers",
							"banks",
							"wallet",
						],
						description='Return a list of results no paging! '
						            'simple: <domain.com>/const/?name=providers',
						examples=[
							OpenApiExample(
									'Example 1',
									summary='Get list banks',
									value='banks'
							),
							OpenApiExample(
									'Example 2',
									summary='Get list social platform providers ',
									value='providers'
							),
							OpenApiExample(
									'Example 3',
									summary='Get list wallet markets',
									value='wallet',
									response_only=True
							),
						]
				),

			],
			responses={
				200: [OpenApiTypes.STR]
			},

			tags=TAGS,
			operation_id=_("Const queries".title()),
			description=_("require: User authenticated to create alias")
	),
}


@extend_schema_view(**docs_)
class ConstApi(viewsets.ViewSet):
	permission_classes = [IsAuthenticated]

	def retrieve(self, request, *args, **kwargs):
		kind = self.request.GET.get("name")
		match kind:
			case "providers":
				dat = list(registry.as_choices())
				dat.append(["other", "other"])
				return Response(dat)

			case "banks":
				return Response(vn_banks)

			case "wallet":
				return Response(wallet_vn)

		return Response()