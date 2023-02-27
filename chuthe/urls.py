from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from django.urls import include, path, re_path

from chuthe.views import ConstApi

urlpatterns = [

    path("const/", ConstApi.as_view({"get": "retrieve"})),
    path("admin/", admin.site.urls),
    path("docs/", include("docs.urls")),
    path("user/", include("user.urls")),
    path("apps/", include("apps.urls")),
    path("alias/", include("alias.urls")),
    path("nof/", include("nof.urls")),
    path("manager/", include("manager.urls")),

    path("activity/", include('actstream.urls')),

    path('auth/', include('chuthe.auth.urls')),
    path('registry/', include('chuthe.auth.reg.urls')),

    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),

    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

handler500 = 'chuthe.errors.exceptions.chuthe_server_5xx'
