import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from racket_stringer.models import String


class Command(BaseCommand):
    help = (
        "Import new strings to the database by scraping an external "
        "website, http://twu.tennis-warehouse.com."
    )

    def handle(self, *args, **options):
        # thank you, Tennis Warehouse University
        base_url = "http://twu.tennis-warehouse.com/learning_center/reporter2.php"

        string_manufacturers = {
            "Babolat",
            "Gamma",
            "Head",
            "Luxilon",
            "MSV",
            "Prince",
            "Solinco",
            "Tecnifibre",
            "Wilson",
            "Yonex",
            "Dunlop",
        }

        payload = {
            "zbrand": "all",
            "display[]": ["xbrand", "xstring"],
            "zstring[]": "all",
            "zref_tension": "all",
            "zhammer": "all",
            "zmaterial": "all",
            "sort1": "brand",
            "sort2": "",
            "sort2": "",
            "sort4": "",
            "sort5": "",
        }

        response = requests.post(base_url, payload)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        string_data_soup = soup.select("#searchresults > tr > td")

        # every element in 'string_data' corresponds to 1 string.
        strings = [r.contents[0] for r in string_data_soup]

        if not strings:
            self.stdout.write(
                self.style.WARNING(
                    "Warning: no strings scraped. HTML of source site may "
                    "have changed."
                )
            )
            return

        for string in strings:
            brand = string.split(" ")[0]
            if brand not in string_manufacturers:
                continue

            s, created = String.objects.get_or_create(
                brand=brand, name=string.split(brand)[1].strip()
            )

            if created:
                self.stdout.write(self.style.SUCCESS('Created String "%s"' % s))
