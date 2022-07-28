from django.db import models


class Alias(models.Model):
    name = models.CharField(max_length=255)
    soft_deleted = models.BooleanField(null=True, default=False)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)

    def delete(self, using=None, keep_parents=False):
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        self.soft_delete = True
        return True

    class Meta:
        verbose_name_plural = "Aliases"
