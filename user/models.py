from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import uuid

import zoneinfo
from django.utils.translation import gettext_lazy as _
from django.conf.global_settings import LANGUAGES


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username or self.email or self.id.__str__()

    phone = PhoneNumberField(blank=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()


class UserSetting(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.PROTECT, primary_key=True)
    lang = models.CharField(max_length=7,
                            choices=LANGUAGES,
                            default=settings.LANGUAGE_CODE)
    tz = models.CharField(
        choices=sorted(
            (item, item) for item in zoneinfo.available_timezones()),
        max_length=64,
        default=settings.USER_TIME_ZONE,
    )

    def __str__(self):
        return f"Setting of {self.user.username or self.user.email or self.user.id.__str__()}"

    class Meta:
        verbose_name_plural = _("User settings")
        ordering = ['-pk']


@receiver(post_save, sender=User)
def user_settings_receiver(sender, instance, created, **kwargs):  # noqa
    if created:
        UserSetting.objects.create(user=instance)
