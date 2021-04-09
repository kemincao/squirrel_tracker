import csv
from django.core.management import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import the squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        #with open(path, 'rt') as f:
        #To be implemented
