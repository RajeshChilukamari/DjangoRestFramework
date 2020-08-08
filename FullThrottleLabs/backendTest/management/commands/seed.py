from django.core.management.base import BaseCommand
from ...serializer import RandomUserFactory, RandomActivityPeriodFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--activities',
                            default=5,
                            type=int,
                            help='The number of fake activities to create.')

    def handle(self, *args, **options):
        for _ in range(options['activities']):
            RandomActivityPeriodFactory()
