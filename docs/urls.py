from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from django.urls import path
from rest_framework import permissions
from django.conf import settings
from chuthe.roles import Privacy
from docs.utils import get_md_docs

INSTRUCTION = "INSTRUCTION"
sub_instruction = ["Overview", "Define"]

urlpatterns = [
    path("", SpectacularRedocView.as_view(), name="redoc"),
    path("api/schema", SpectacularAPIView.as_view(
        permission_classes=[permissions.IsAuthenticated],
        custom_settings={
            "EXTENSIONS_ROOT": {
                "x-tagGroups": [
                    {"name": INSTRUCTION,
                     "tags": sub_instruction},
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

                ],

            },
            "TAGS": [
                {"name": sub_instruction[0],
                 "description": get_md_docs("instruction.md"),
                 "x-traitTag": True
                 },
                {"name": sub_instruction[1],
                 "description": get_md_docs("define.md"),
                 "x-traitTag": True
                 },
            ],

        }
    ),
         name="schema"
         ),
]
