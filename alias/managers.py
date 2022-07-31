from django.db import models
from django.utils import timezone


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