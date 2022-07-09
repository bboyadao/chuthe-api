from rest_framework import fields, serializers

from user.models import User


class UserSer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User


class RegSer(serializers.ModelSerializer, serializers.Serializer):
    class Meta:
        model = User
        fields = ("password", "username", "email", "phone")

    password = serializers.CharField()

    def create(self, validated_data):
        pass

