from rest_framework.routers import DefaultRouter
from user.views import UserView

router = DefaultRouter()
router.register('', UserView)

urlpatterns = list()
urlpatterns += router.urls

