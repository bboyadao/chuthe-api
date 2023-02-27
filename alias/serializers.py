from allauth.socialaccount.models import SocialAccount
from rest_framework import serializers
from alias.models import Alias, ContactInformation, Links, PaymentInformation, PaymentBrand


class PaymentBrandSer(serializers.ModelSerializer):
    class Meta:
        model = PaymentBrand
        fields = "__all__"


class PaymentInformationSer(serializers.ModelSerializer):
    infor = PaymentBrandSer(source="dst")

    class Meta:
        model = PaymentInformation
        fields = "__all__"


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
            "payments",
            "links",
            "created_at",
            "created_by",
        ]
        lookup_field = "path"

    socials = SocialAccountSer(many=True, read_only=True)
    contact = ContactInformationSer(read_only=True)
    links = LinksSer(read_only=True, many=True)
    payments = PaymentInformationSer(many=True, read_only=True)


class UserPatchAliasSer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        exclude = ["id", "soft_deleted", "created_by", "user", "path"]


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


class ContactSer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = "__all__"


class LinkSer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"
