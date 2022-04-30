from rest_framework import viewsets
from apps.serializers import AppSer
from oauth2_provider.models import get_application_model
from rest_framework.permissions import IsAuthenticated


class Application(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = get_application_model().objects.all()
    serializer_class = AppSer
