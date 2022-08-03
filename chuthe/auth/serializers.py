from rest_framework import serializers


class LogoutRequestSerialiser(serializers.Serializer):
    refresh = serializers.CharField()


class ShitResponseSerialiser(serializers.Serializer):
    detail = serializers.CharField()
    status = serializers.IntegerField()