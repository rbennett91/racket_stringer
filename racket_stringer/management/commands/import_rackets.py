import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from racket_stringer.models import Racket


class Command(BaseCommand):
    help = 'Import new strings to the database by scraping an external '\
           'website, https://klipperusa.com.'

    def handle(self, *args, **options):
        # thank you, KLIPPER USA
        base_url = "https://klipperusa.com/pages/{url_ending}"

        racket_manufacturers = [
            {
                'name': 'Wilson',
                'url_ending': 'wilson-tennis-racquet-patterns',
            },
            {
                'name': 'Prince',
                'url_ending': 'prince-tennis-racquet-patterns',
            },
            {
                'name': 'Babolat',
                'url_ending': 'babolat-tennis-racquet-patterns',
            },
            {
                'name': 'Head',
                'url_ending': 'head-tennis-racquet-patterns',
            },
            {
                'name': 'Yonex',
                'url_ending': 'yonex-tennis-racquet-patterns',
            },
        ]

        for racket_manufacturer in racket_manufacturers:
            response = requests.get(
                base_url.format(url_ending=racket_manufacturer['url_ending']),
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'lxml')
            racket_data_soup = soup.select("table > tbody > tr > td")

            # every set of 8 elements in 'racket_data' corresponds to 1 racket.
            # ie. racket_data[0:8] holds all data for the first racket.
            racket_data = [r.contents[0] for r in racket_data_soup]
            rackets = [
                racket_data[x:x+8] for x in range(0, len(racket_data), 8)
            ]

            if not rackets:
                self.stdout.write(
                    self.style.WARNING(
                        'Warning: no rackets scraped. HTML of source site may '
                        'have changed.'
                    )
                )
                return

            for racket in rackets:
                r, created = Racket.objects.get_or_create(
                    brand=racket_manufacturer['name'],
                    model=racket[0],
                    defaults={
                        'recommended_tension_lbs': racket[1],
                        'string_length': racket[2],
                        'string_pattern': racket[3],
                        'main_holes_skipped': racket[4],
                        'main_holes_tied': racket[5],
                        'cross_holes_started': racket[6],
                        'cross_holes_tied': racket[7],
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS('Created Racket "%s"' % r)
                    )
