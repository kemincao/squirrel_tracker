import csv
import datetime
from django.core.management import BaseCommand

from sightings.models import Squirrels

class Command(BaseCommand):
    help = 'Export the squirrel data'
  
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'w', newline='') as fp:
            attributes = ['Y',
                        'X',
            		'Unique_squirrel_id',
            		'Shift',
    			'Date',
  			'Age',
            		'Fur',
            		'Location',
                        'Specific_location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From']
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Squirrels.objects.all():
                writer.writerow([getattr(row, attr) for attr in attributes])

        self.stdout.write(self.style.SUCCESS('Squirrel Export Successful'))
