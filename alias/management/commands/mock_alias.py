from django.core.management.base import BaseCommand
from alias.models import Alias
from user.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Mock user and aliases'
    RANGE = 5

    def create_bulk_users(self):
        bulk = []
        for i in range(1, self.RANGE):
            me = {
                "username": f"test_user_{i}",
                "password": make_password(f"test_user_{i}")
            }
            bulk.append(User(**me))
        return User.objects.bulk_create(bulk)

    def create_bulk_aliases(self):
        users = self.create_bulk_users()
        bulk = []
        for i, user in enumerate(users):
            alias = {
                "name": f"test_alias_{i}",
                "user": user
            }
            bulk.append(Alias(**alias))
        return Alias.objects.bulk_create(bulk)

    def handle(self, *args, **options):
        self.create_bulk_aliases()
        self.stdout.write(self.style.SUCCESS(f"Created and Linked {self.RANGE} Users and alias"))

