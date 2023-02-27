from allauth.socialaccount.models import SocialAccount
from drf_spectacular.types import OpenApiTypes
from rest_framework import filters

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from alias.docs.alias import alias_docs
from alias.docs.contact import contact_docs
from alias.docs.link import link_docs
from alias.docs.payment import payment_docs
from alias.docs.social import social_docs

from alias.models import Alias, PaymentInformation, Links, ContactInformation
from alias.paging import AliasUserPagination, TinyPagination
from alias.permissions import ThemSelf, PaidMember, Mine
from alias.serializers import UserCreateAliasSer, UserRetrieveAliasSer, UserPatchAliasSer, UserListAliasSer, \
    ChangePathSer, SocialAccountSer, ContactSer, LinkSer, PaymentInformationSer
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

    @action(methods=["patch", 'options'], detail=True, permission_classes=[ThemSelf, PaidMember])
    def change_path(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.update(self.get_object(), serializer.data)
        return Response(status.HTTP_200_OK)

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

            case "change_path": return ChangePathSer

            case _: return UserRetrieveAliasSer


@extend_schema(
    parameters=[OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)])
@extend_schema_view(**social_docs)
class SocialView(viewsets.ModelViewSet):
    serializer_class = SocialAccountSer
    queryset = SocialAccount.objects.filter()
    permission_classes = [Mine, ]
    pagination_class = TinyPagination

    def get_queryset(self):
        a = Alias.objects.get(path=self.kwargs.get("user_alias_path"))
        return a.socials.all().order_by("id")


@extend_schema(
    parameters=[OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)])
@extend_schema_view(**payment_docs)
class PaymentView(viewsets.ModelViewSet):
    serializer_class = PaymentInformationSer
    queryset = PaymentInformation.objects.filter()
    permission_classes = [Mine, ]
    pagination_class = TinyPagination

    def get_queryset(self):
        a = Alias.objects.get(path=self.kwargs.get("user_alias_path"))
        return a.payments.all().order_by("id")


@extend_schema(
    parameters=[OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)])
@extend_schema_view(**contact_docs)
class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSer
    queryset = ContactInformation.objects.filter()
    permission_classes = [Mine, ]
    pagination_class = TinyPagination

    def get_queryset(self):
        a = Alias.objects.get(path=self.kwargs.get("user_alias_path"))
        return a.contacts.all().order_by("id")


@extend_schema(
    parameters=[OpenApiParameter(name="user_alias_path", type=OpenApiTypes.STR, location=OpenApiParameter.PATH)])
@extend_schema_view(**link_docs)
class LinkView(viewsets.ModelViewSet):
    serializer_class = LinkSer
    queryset = Links.objects.filter()
    permission_classes = [Mine, ]
    pagination_class = TinyPagination

    def get_queryset(self):
        a = Alias.objects.get(path=self.kwargs.get("user_alias_path"))
        return a.links.all().order_by("id")
