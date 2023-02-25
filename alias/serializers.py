from rest_framework import serializers
from alias.models import Alias, ValueAilasValue


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


class CreateAliasAttrSer(serializers.Serializer):
    custom_key = serializers.CharField(required=False, allow_null=True)
    key_id = serializers.IntegerField(required=False, allow_null=True)
    value = serializers.CharField()

    def validate_key(self, key):
        if key not in ValueAilasValue.KeyAttr.values:
            raise serializers.ValidationError("System not support this type")
        return key

    def validate(self, data):
        key = data.get("key")
        custom_key = data.get("custom_key")
        if custom_key and key:
            raise serializers.ValidationError("not both")
        return data


class Attrs(serializers.Serializer):
    attrs = serializers.ListSerializer(child=CreateAliasAttrSer())

    def validate_attrs(self, attrs):
        return attrs

    def create(self):
        attrs = self.validated_data.get("attrs")
        datas = [ValueAilasValue(**i) for i in attrs]
        aa = ValueAilasValue.objects.bulk_create(datas)
        print(aa)
        return 200