from oauth2_provider.views import ApplicationRegistration
from rest_framework import viewsets
from apps.serializers import AppSer
from oauth2_provider.models import get_application_model


class Application(viewsets.ModelViewSet):
    model = get_application_model()
    queryset = model.objects.all()
    serializer_class = AppSer
