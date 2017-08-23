from django.core.management.base import BaseCommand, CommandError
from masters import models


class Command(BaseCommand):
    help = 'Check ticket threshold time'

    def add_arguments(self, parser):
        parser.add_argument('ticket_id', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"'))