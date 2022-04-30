from oauth2_provider.models import get_application_model
from rest_framework import serializers
from rest_framework.exceptions import APIException, NotFound


class AppSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = get_application_model()

    def create(self, validated_data):
        req = self.context.get("request")

        if req:
            if not req.user.is_anonymous:
                validated_data["user"] = req.user
            else:
                raise NotFound(detail="Error user not found", code="404")
            return super().create(validated_data)
        raise APIException("Unknown Error")
