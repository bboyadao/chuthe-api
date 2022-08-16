from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, permissions

from alias.docs import manage_alias_docs
from alias.models import Alias
from alias.paging import AliasUserPagination
from alias.serializers import UserCreateAliasSer, UserRetriveAliasSer, UserUpdateAliasSer
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema_view(**manage_alias_docs)
class ManageAlias(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    pagination_class = AliasUserPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "des", "path"]

    def get_queryset(self):
        return Alias.objects.all()

    def perform_destroy(self, instance):
        instance.soft_deleted = True
        instance.save()

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_class(self) -> UserCreateAliasSer | UserRetriveAliasSer | UserUpdateAliasSer | None:
        match self.action:
            case "create":
                return UserCreateAliasSer
            case "retrieve" | "list":
                return UserRetriveAliasSer
            case "update" | "partial_update":
                return UserUpdateAliasSer
            case _: return UserRetriveAliasSer
