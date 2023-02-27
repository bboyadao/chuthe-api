from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, permissions

from alias.models import Alias
from alias.paging import AliasUserPagination
from alias.serializers import UserCreateAliasSer, UserRetrieveAliasSer, UserPatchAliasSer
from rest_framework import filters

from manager.docs.alias import manage_alias_docs


@extend_schema_view(**manage_alias_docs)
class ManageAlias(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    pagination_class = AliasUserPagination
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["name", "des", "path"]
    lookup_field = "path"

    def get_queryset(self):
        return Alias.objects.all()

    def perform_destroy(self, instance):
        instance.soft_deleted = True
        instance.save()

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_class(self) -> UserCreateAliasSer | UserRetrieveAliasSer | UserPatchAliasSer | None:
        match self.action:
            case "create":
                return UserCreateAliasSer
            case "retrieve" | "list":
                return UserRetrieveAliasSer
            case "update" | "partial_update":
                return UserPatchAliasSer
            case _: return UserRetrieveAliasSer
