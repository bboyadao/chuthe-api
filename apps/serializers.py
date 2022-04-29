from oauth2_provider.models import get_application_model
from rest_framework import serializers


class AppSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = get_application_model()

