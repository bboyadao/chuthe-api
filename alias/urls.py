from rest_framework.routers import DefaultRouter

from alias.views import UserAlias

app_name = "Alias"

router = DefaultRouter()
router.register("", UserAlias, "user_alias")

urlpatterns = router.urls
