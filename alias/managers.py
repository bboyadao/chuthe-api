from django.db import models
import uuid


class AliasManager(models.Manager):

    def is_existed_custom_path(self, path):
        if self.filter(path=path).exists():
            return True
        return False

    def gen_alias_id(self, obj):
        user_pk = None
        if isinstance(obj, dict):
            user_pk = obj["user"].pk

        if isinstance(obj, self.model):
            user_pk = obj.user.pk

        uniq = f"{user_pk}{str(uuid.uuid4())[:8]}"

        if self.get_queryset().filter(path=uniq).exists():
            return self.gen_alias_id(obj)
        else:
            return uniq

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

    def my_aliases(self, user):
        return self.get_queryset().filter(user=user, soft_deleted=False).order_by("pk")
