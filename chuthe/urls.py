from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


urlpatterns = [
    path("admin/", admin.site.urls),
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),

    path("docs/", include("docs.urls")),
    path("user/", include("user.urls")),
    path("apps/", include("apps.urls")),
    path("alias/", include("alias.urls")),

    # path('auth', include('dj_rest_auth.urls')),
    path('auth/', include('chuthe.auth.urls')),
    path('registry/', include('chuthe.auth.reg.urls')),
    # path('registry/', include('dj_rest_auth.registration.urls')),

    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
