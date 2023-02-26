from allauth.socialaccount.providers import registry

from rest_framework import viewsets
from rest_framework.response import Response


class ConstApi(viewsets.ViewSet):

	def retrieve(self, request, *args, **kwargs):
		kind = self.request.GET.get("name")
		match kind:
			case "providers":
				dat = list(registry.as_choices())
				dat.append(["other", "other"])
				return Response(dat)
		return Response()
