from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets

from alias.docs import alias_docs
from alias.models import Alias
from alias.paging import AliasUserPagination
from alias.permissions import ThemSelf
from alias.serializers import UserCreateAliasSer, UserRetriveAliasSer, UserUpdateAliasSer
from django.conf import settings

loger = settings.LOGGER


@extend_schema_view(**alias_docs)
class UserAlias(viewsets.ModelViewSet):
    permission_classes = [ThemSelf, ]
    pagination_class = AliasUserPagination

    def get_queryset(self):
        return Alias.objects.my_aliases(user=self.request.user)

    def perform_destroy(self, instance):
        instance.soft_deleted = True
        instance.save()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self) -> UserCreateAliasSer | UserRetriveAliasSer | UserUpdateAliasSer | None:
        match self.action:
            case "create":
                return UserCreateAliasSer
            case "retrieve" | "list":
                return UserRetriveAliasSer
            case "update" | "partial_update":
                return UserUpdateAliasSer
            case _: return UserRetriveAliasSer


