from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import User, UserSettings
from user.docs import user_docs, user_settings_docs
from user.perms import MySelf
from user.serializers import MeSer, UserUpdateSer, UserSettingSer
from user.throttles import FreeBehavior
from rest_framework import permissions


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


@extend_schema_view(**user_settings_docs)
class UserSettingView(viewsets.ViewSet):
    model = UserSettings
    permission_classes = [IsAuthenticated, MySelf]
    serializer_class = UserSettingSer

    def get_object(self):
        return self.request.user.settings

    def retrieve(self, *args, **kwargs):
        serializer = UserSettingSer(self.get_object())
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UserSettingSer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @staticmethod
    def perform_update(serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
