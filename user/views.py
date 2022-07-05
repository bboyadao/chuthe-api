from django.views.generic import detail
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from user.models import User
from user.docs import user_docs


@extend_schema_view(**user_docs)
class UserView(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()

    @action(detail=False, method="POST", serializer_class=None)
    def register(self):

        return Response({})
