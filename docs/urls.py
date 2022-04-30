from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from django.urls import path


urlpatterns = [
    path("docs/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
]
