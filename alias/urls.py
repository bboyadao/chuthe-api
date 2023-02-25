from rest_framework_extensions.routers import ExtendedSimpleRouter
from alias.views import UserAlias

app_name = "Alias"


router = ExtendedSimpleRouter()
router.register("", UserAlias, "user_alias")

urlpatterns = router.urls
