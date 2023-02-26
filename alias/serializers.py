from allauth.socialaccount.models import SocialAccount
from rest_framework import serializers
from alias.models import Alias, ValueAilasValue, ContactInformation, Links


class LinksSer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ["id", "val", "alt"]


class ContactInformationSer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = "__all__"


class SocialAccountSer(serializers.ModelSerializer):
    provider_id = serializers.CharField(source="provider")
    name = serializers.SerializerMethodField()

    def get_name(self, ins):
        return ins.get_provider_display()

    class Meta:
        model = SocialAccount
        fields = ["id", "uid", "provider_id", "name"]


class UserCreateAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["name", "des"]


class UserListAliasSer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Alias:user_alias-detail", lookup_field="path")

    class Meta:
        model = Alias
        fields = ["path", "name", "url"]


class UserRetrieveAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = [
            "name",
            "des",
            "default",
            "socials",
            "contact",
            "links",
            "created_at",
            "created_by",
        ]
        lookup_field = "path"

    socials = SocialAccountSer(many=True, read_only=True, source="socialaccount")
    contact = ContactInformationSer(read_only=True)
    links = LinksSer(read_only=True, many=True, source="links_set")


class UserPatchAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        exclude = ["id", "soft_deleted", "created_by", "user", "path"]


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
        return 200


class ChangePathSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ["path"]

    def validate(self, data):
        path = data.get("path", None)
        if Alias.objects.is_existed_custom_path(path=path):
            raise serializers.ValidationError("existed")
        return data

    def update(self, instance, validated_data):
        super(ChangePathSer, self).update(instance, validated_data)