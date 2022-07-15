from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include("docs.urls")),
    path("user/", include("user.urls")),
    path("apps/", include("apps.urls")),

    path('auth/', include('dj_rest_auth.urls')),
    path('signup_normal/', include('dj_rest_auth.registration.urls')),
    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
