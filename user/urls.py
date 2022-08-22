from django.urls import path

from user.views import UserView, UserSettingView
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()
(
    router.register(r'', UserView, basename='user')

)
urlpatterns = router.urls
urlpatterns += [
    path("<uuid:user_pk>/settings/", UserSettingView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),

]
