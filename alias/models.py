from django.db import models
from django.utils.translation import gettext as _

from alias.managers import AliasManager


class Alias(models.Model):
    objects = AliasManager()
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=128)
    des = models.TextField(max_length=500, null=True)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
    created_by = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    soft_deleted = models.BooleanField(null=True, default=False)

    class Meta:
        verbose_name_plural = _("Aliases")
