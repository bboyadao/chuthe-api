from django.core.checks import Error, register, Tags
import os
from django.contrib.sites.models import Site

from alias.management.commands.load_config import list_sites


def get_cred():
    client_id = os.getenv("GOOGLE_CLIENT_ID", None)
    client_sec = os.getenv("GOOGLE_CLIENT_SEC", None)
    return all([client_sec, client_id]), client_id, client_sec


@register(deploy=True)
def envs_check(app_configs, **kwargs):  # noqa
    errors = []
    list_env = ("SECRET_KEY",
                "DEBUG",
                "BROKER_SCHEMA",
                "BROKER_USER",
                "BROKER_PASSWORD",
                "BROKER_HOST",
                "BROKER_PORT",
                "CELERY_CACHE_BACKEND",
                "DATABASE_NAME",
                "DATABASE_URL",
                "DATABASE_PORT",
                "DATABASE_USER",
                "DATABASE_PASSWORD", )
    for i in list_env:
        e = os.getenv(i, None)
        if not e:
            errors.append(Error(f"Missed env var `{i}`", id="CHUTHE.E001"))
    return errors


@register(deploy=True, tag=Tags.sites)
def sites_check(app_configs, **kwargs):  # noqa
    _bool, client_id, client_sec = get_cred()
    assert _bool is True
    errors = []
    domains = [i['domain'] for i in list_sites]
    sites = Site.objects.filter(domain__in=domains)
    if sites.count() != domains.__len__():
        errors.append(
            Error(
                "Sites config not match `python manage.py loaddata dumps/sites.json or python manage.py load_config`",
                id="CHUTHE.E002"))
    return errors
