import csv
import datetime
from django.core.management import BaseCommand

from sightings.models import Squirrels

class Command(BaseCommand):
    help = 'Import the squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt') as f:
            data = csv.reader(f, dialect='excel')
            next(data)
            data_info = list(data)
            unique_id = list()
            for row in data_info:
                if row[2] in unique_id:
                    continue
                else:
                    squirrel = Squirrels.objects.get_or_create(
                        X = float(row[0]),
                        Y = float(row[1]),
                        Unique_squirrel_id = row[2],
                        Shift = row[4],
                        Date = datetime.datetime.strptime(row[5],'%m%d%Y'),
                        Age = row[7],
                        Fur = row[8],
                        Location = row[12],
                        Specific_location = row[14],
                        Running = (row[15] == 'true'),
                        Chasing = (row[16] == 'true'),
                        Climbing = (row[17] == 'true'),
                        Eating = (row[18] == 'true'),
                        Foraging = (row[19] == 'true'),
                        Other_Activities = row[20],
                        Kuks = (row[21] == 'true'),
                        Quaas = (row[22] == 'true'),
                        Moans = (row[23] == 'true'),
                        Tail_Flags = (row[24] == 'true'),
                        Tail_Twitches = (row[25] == 'true'),
                        Approaches = (row[26] == 'true'),
                        Indifferent = (row[27] == 'true'),
                        Runs_From = (row[28] == 'true'),
                        )  
                unique_id.append(row[2])

            self.stdout.write(self.style.SUCCESS('Data Import Done'))
