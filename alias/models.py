from django.db import models
from django.utils.translation import gettext as _

from alias.managers import AliasManager


class Alias(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField(max_length=500, null=True)
    soft_deleted = models.BooleanField(null=True, default=False)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
    path = models.CharField(max_length=128)
    objects = AliasManager()

    class Meta:
        verbose_name_plural = _("Aliases")

    def delete(self, using=None, keep_parents=False):
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        self.soft_delete = True
        return True
