from django.core.management.base import BaseCommand
from scripts.scrap import get_snp500


class Command(BaseCommand):
    args = ''
    help = 'scrap and update data.'

    def handle(self, *args, **options):
        # do something here
        get_snp500()
        print('Success')
