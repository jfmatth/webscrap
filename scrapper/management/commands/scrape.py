from django.core.management.base import BaseCommand

from scrapper.models import Scrape, Results

from django.utils import timezone

from datetime import datetime
import requests

class Command(BaseCommand):
    help = "Scrapes <website> for <keyword>"

    def handle(self, *args, **options):
        print(f'Scrapping all sites for keywords' )

        for s in Scrape.objects.all():
            print( f'Scrapping {s.site} for {s.keyword}' )

            r = requests.get(s.site)
            n = r.text.count(s.keyword)

            x = Results(
                Scrape = s,
                date = timezone.now(),
                contents = r.text,
                matches = n                
            )
            x.save()