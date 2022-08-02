from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from django.urls import path
from rest_framework import permissions
from django.conf import settings
from chuthe.roles import Privacy


urlpatterns = [
    path("", SpectacularRedocView.as_view(), name="redoc"),
    path("api/schema", SpectacularAPIView.as_view(
        permission_classes=[permissions.IsAuthenticated],
        # urlconf=...,
        custom_settings={
            "EXTENSIONS_ROOT": {"x-tagGroups": [
                {
                    "name": Privacy.ADMIN,
                    "tags": settings.DOCS_TAG[Privacy.ADMIN.value],
                },
                {
                    "name": Privacy.STAFF,
                    "tags": settings.DOCS_TAG[Privacy.STAFF.value],
                },
                {
                    "name": Privacy.USER,
                    "tags": settings.DOCS_TAG[Privacy.USER.value],
                },
                {
                    "name": Privacy.PUBLIC,
                    "tags": settings.DOCS_TAG[Privacy.PUBLIC.value],
                },
            ], },
        }
    ),
         name="schema"
         ),
]
