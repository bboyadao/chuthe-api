from django.core.management.base import BaseCommand, CommandError
from alias.models import Alias
from user.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Mock user and aliases'
    RANGE = 100
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def create_bulk_users(self):
        bulk = []
        for i in range(1, self.RANGE):
            me = {
                "username": f"user_name_{i}",
                "password": make_password(f"user_name_{i}")
            }
            bulk.append(User(**me))
        self.stdout.write(self.style.SUCCESS(f"Created {self.RANGE} Users"))
        return User.objects.bulk_create(bulk)

    def create_bulk_aliases(self):
        users = self.create_bulk_users()
        bulk = []
        for i, user in enumerate(users):
            alias = {
                "name": f"name_{i}",
                "user": user
            }
            bulk.append(Alias(**alias))
        self.stdout.write(self.style.SUCCESS(f"Linked {self.RANGE} Users and alias"))
        return Alias.objects.bulk_create(bulk)

    def handle(self, *args, **options):
        self.create_bulk_aliases()
