from rest_framework.routers import DefaultRouter

from manager.views import ManageAlias

app_name = "Manager"

router = DefaultRouter()
router.register("alias", ManageAlias, "manage_alias")

urlpatterns = router.urls
