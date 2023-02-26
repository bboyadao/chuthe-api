from django.db import models
from rest_framework.reverse import reverse_lazy

from alias.managers import AliasManager
from django.utils.translation import gettext_lazy as _
from allauth.socialaccount.models import SocialAccount


class ContactInformation(models.Model):
    phone = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    add = models.CharField(max_length=255)


class Links(models.Model):
    alias = models.ForeignKey("alias.Alias", on_delete=models.CASCADE)
    alt = models.TextField(help_text=_("Description"), null=True, blank=True)
    val = models.URLField()


class Alias(models.Model):
    objects = AliasManager()
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=128)
    des = models.TextField(max_length=500, null=True)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
    created_by = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    default = models.BooleanField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    soft_deleted = models.BooleanField(null=True, default=False)
    socialaccount = models.ManyToManyField(SocialAccount)
    contact = models.ForeignKey(
        "alias.ContactInformation",
        on_delete=models.CASCADE,
        null=True, blank=True,
        default=None
    )

    def get_absolute_url(self):
        return reverse_lazy("user_alias-detail", self.path)

    class Meta:
        verbose_name_plural = _("Aliases")
        ordering = ['-pk']
        unique_together = ["id", "path"]
        index_together = unique_together


class ValueAilasValue(models.Model):
    class KeyAttr(models.IntegerChoices):
        # custom = None, _("custom")
        phone = 1, _("personal phone".title())
        work_phone = 2, _("work phone".title())
        web = 3, _("website".title())
        face = 4, _("facebook".title())
        twitter = 5, _("twitter".title())
        insta = 6, _("instagram".title())
        tiktok = 7, _("tiktok".title())
        ld = 8, _("linked in".title())
        payment = 99, _("payment".title())
        other = 100, _("other".title())

    key = models.SmallIntegerField(choices=KeyAttr.choices, null=True, blank=True)
    custom_key = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, blank=True)
    index = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.get_key_display() if self.key else self.custom_key}: {self.value}"


class PaymentBrand(models.Model):
    name = models.CharField(max_length=255)
    ico = models.CharField(max_length=1024, null=True, blank=True)


class PaymentAliasAttr(models.Model):
    alias = models.ForeignKey("alias.Alias", on_delete=models.CASCADE)
    dst = models.ForeignKey("alias.PaymentBrand", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
