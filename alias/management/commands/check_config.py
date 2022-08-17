import os

from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


def check_cred():
    client_id = os.getenv("GOOGLE_CLIENT_ID", None)
    client_sec = os.getenv("GOOGLE_CLIENT_SEC", None)
    return all([client_sec, client_id]), client_id, client_sec


class Command(BaseCommand):
    help = 'Check config and initial data'

    def force_create_google_app_client(self):
        pass

    def handle(self, *args, **options):
        _bool, client_id, client_sec = check_cred()
        assert _bool is True
        l = [

            {"domain": "chuthe.com", "name": "chuthe.prod"},
            {"domain": "staging.chuthe.com", "name": "staging.chuthe"},
            {"domain": "test.chuthe.com", "name": "test.chuthe"},
            {"domain": "local.chuthe.com", "name": "local.chuthe"},
            {"domain": "localhost:4200", "name": "localhost"},
            {"domain": "localhost:8000", "name": "localhost"}
        ]
        domains = [i['domain'] for i in l]
        sites = Site.objects.filter(domain__in=domains)
        if sites.count() != domains.__len__():
            sites.delete()
            # force create domain
            _l = [Site(**i) for i in l]
            s = Site.objects.bulk_create(_l)
            self.stdout.write(self.style.SUCCESS(f"Created {len(s)} domains"))
            for provider in providers.registry.get_list():
                if provider.id == "google":
                    app = SocialApp.objects.create(
                        provider=provider.id,
                        name="Google Api",
                        client_id=client_id,
                        key="",
                        secret=client_sec)
                    app.sites.set(s)
