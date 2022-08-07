from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from django.urls import include, path, re_path


urlpatterns = [
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]
