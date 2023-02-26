from rest_framework import filters

from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from alias.docs import alias_docs
from alias.models import Alias
from alias.paging import AliasUserPagination
from alias.permissions import ThemSelf
from alias.serializers import UserCreateAliasSer, UserRetrieveAliasSer, UserPatchAliasSer, UserListAliasSer, Attrs
from django.conf import settings

loger = settings.LOGGER


@extend_schema_view(**alias_docs)
class UserAlias(viewsets.ModelViewSet):
    permission_classes = [ThemSelf, ]
    pagination_class = AliasUserPagination
    search_fields = ["des", "name"]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["created_at"]
    lookup_field = "path"

    @action(methods=["post", "get", 'options'], detail=True)
    def attrs(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.create()
        return Response({"ok": "ok"})

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        return Alias.objects.my_aliases(user=self.request.user)

    def perform_destroy(self, instance):
        instance.soft_deleted = True
        instance.save()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self) -> UserListAliasSer | UserCreateAliasSer | UserRetrieveAliasSer | UserPatchAliasSer | None:
        match self.action:
            case "create":
                return UserCreateAliasSer
            case "retrieve":
                return UserRetrieveAliasSer
            case "list":
                return UserListAliasSer
            case "partial_update":
                return UserPatchAliasSer
            case "attrs": return Attrs
            case _: return UserRetrieveAliasSer


