from datetime import date

from accounts.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Deletes inactive accounts from database."

    def handle(self, *args, **options):
        users = User.objects.inactive().filter(delete_date=date.today())

        self.stdout.write(
            self.style.NOTICE(f"Queried {users.count()} accounts to delete.")
        )
        users.delete()
        self.stdout.write(self.style.SUCCESS("Accounts deleted succesfully."))
