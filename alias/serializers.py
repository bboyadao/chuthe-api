from rest_framework import serializers
from alias.models import Alias


class UserCreateAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["name", "des"]


class UserListAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["path", "name"]


class UserRetriveAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        exclude = ["soft_deleted", "user"]
        lookup_field = "path"


class UserPatchAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        exclude = ["id", "soft_deleted", "created_by", "user"]
