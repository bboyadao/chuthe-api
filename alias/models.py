from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class AliasManager(models.Manager):

    def gen_alias_id(self, obj):
        user_pk = None
        if isinstance(obj, dict):
            user_pk = obj["user"].pk

        if isinstance(obj, self.model):
            user_pk = obj.user.pk

        return f"{user_pk}{int(timezone.now().timestamp() * 1000000)}"

    def create(self, **obj_data):
        obj_data['path'] = self.gen_alias_id(obj_data)
        return super().create(**obj_data)

    def bulk_create(self, objs, **kwargs):
        new_objs = []
        for obj in objs:
            n_obj = obj
            n_obj.path = self.gen_alias_id(obj)
            new_objs.append(n_obj)
        return super().bulk_create(new_objs, **kwargs)


class Alias(models.Model):
    name = models.CharField(max_length=255)
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
