from rest_framework import viewsets

from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import User
from user.docs import user_docs
from user.perms import MySelf
from user.serializers import MeSer, UserUpdateSer
from user.throttles import FreeBehavior
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import APIException


@extend_schema_view(**user_docs)
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MeSer
    permission_classes = [IsAuthenticated, MySelf]

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return UserUpdateSer
        return super().get_serializer_class()

    def get_current_user(self):
        return self.request.user or None

    @action(detail=False,
            methods=["GET"],
            throttle_classes=[FreeBehavior])
    def me(self, request, *args, **kwargs):
        return Response(self.get_serializer(self.get_current_user()).data)
