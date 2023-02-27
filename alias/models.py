from django.db import models

from alias.managers import AliasManager
from django.utils.translation import gettext_lazy as _
from allauth.socialaccount.models import SocialAccount


class PaymentBrand(models.Model):
    class PaymentKind(models.IntegerChoices):
        bank = 1, _("bank")
        digital_wallet = 2, _("digital wallet")
    kind = models.SmallIntegerField(choices=PaymentKind.choices)
    name = models.CharField(max_length=255)
    iden = models.CharField(max_length=2, null=True, blank=True)


class PaymentInformation(models.Model):
    dst = models.ForeignKey("alias.PaymentBrand", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    default = models.BooleanField(default=False)


class ContactInformation(models.Model):
    kind = models.CharField(max_length=25)
    value = models.CharField(max_length=1024)


class Links(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
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
    socials = models.ManyToManyField(SocialAccount)
    contacts = models.ManyToManyField("alias.ContactInformation")
    payments = models.ManyToManyField("alias.PaymentInformation")
    links = models.ManyToManyField("alias.Links")

    class Meta:
        verbose_name_plural = _("Aliases")
        ordering = ['-pk']
        unique_together = ["id", "path"]
        index_together = unique_together
