from django.db.models.signals import post_save
from django.contrib.auth.models import UserManager as UM


class UserManager(UM):
    def bulk_create(self, objs, **kwargs):
        a = super().bulk_create(objs, **kwargs)
        for i in objs:
            post_save.send(i.__class__, instance=i, created=True)
        return a
