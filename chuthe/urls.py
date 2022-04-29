from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("user/", include("user.urls")),

    # path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("apps/", include("apps.urls")),

    re_path(r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve,
            {"document_root": settings.STATIC_ROOT}),
]
