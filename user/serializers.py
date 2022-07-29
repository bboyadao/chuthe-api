from rest_framework import serializers

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


class MeSer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password",
                   "is_superuser",
                   "is_staff",
                   "date_joined",
                   "user_permissions"]


class UserUpdateSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone",
            "email",
        ]
