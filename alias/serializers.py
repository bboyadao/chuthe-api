from rest_framework import serializers
from alias.models import Alias


class UserCreateAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["name", "des"]


class UserRetriveAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["id", "path", "name",  "des"]


class UserUpdateAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        exclude = ["name", "des"]
