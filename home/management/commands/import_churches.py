import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from home.models import Church


class Command(BaseCommand):
    help = 'Import churches from csv'

    def handle(self, *args, **kwargs):
        Church.objects.all().delete()
        csv_path = os.path.join(
            settings.BASE_DIR,
            'docs',
            'NorthCarnmarthDeaneryLocations.csv',
        )
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                lat = row.get('Latitude')
                lon = row.get('Longitude')
                latitude = float(lat) if lat else None
                longitude = float(lon) if lon else None
                Church.objects.update_or_create(
                    name=row['Name'],
                    postcode=row['Postcode'],
                    defaults={
                        'address': row['Location'],
                        'latitude': latitude,
                        'longitude': longitude,
                        'contact': '',  # Add contact if available in CSV
                    }
                )
                count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Imported Churches: {count}')
            )
