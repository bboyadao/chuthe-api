from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import zoneinfo
from django.utils.translation import gettext_lazy as _

from django.conf.global_settings import LANGUAGES
from django.conf import settings


class User(AbstractUser):

    def __str__(self):
        return self.username

    phone = PhoneNumberField(blank=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

# class LANGS(models.TextChoices):
#     def __init__(self):
    #         sorted(setattr(self.item = item) for item in zoneinfo.available_timezones())


class Profile(models.Model):
    user = models.ForeignKey("user.User", null=True, on_delete=models.PROTECT)
    # dob = models.DateField(blank=True)
    # full_name = models.TextField(blank=True)
    # email = models.EmailField(verbose_name=_(''), null=True)
    # phone = models.CharField(max_length=12, null=True)
    # address = models.TextField(blank=True)
    # lang = models.CharField(max_length=7,
    #                         choices=LANGUAGES,
    #                         default=settings.LANGUAGE_CODE)
    # tz = models.CharField(
    #     choices=sorted(
    #         (item, item) for item in zoneinfo.available_timezones()),
    #     max_length=64,
    #     default=settings.USER_TIME_ZONE,
    # )
    
