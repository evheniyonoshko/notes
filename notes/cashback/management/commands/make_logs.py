import json

from django.core.management.base import BaseCommand

from notes.cashback.models import Log

class Command(BaseCommand):
    help = (
        'Save logs from json to database'
    )

    def handle(self, *args, **options):
        with open('logs.json') as json_file:
            data = json.load(json_file)
            Log.objects.bulk_create(
                [
                    Log(
                        client_id=item['client_id'],
                        user_agent=item['User-Agent'],
                        document_location=item['document.location'],
                        document_referer=item['document.referer'],
                        date=item['date']
                    )
                    for item in data
                ]
            )
        self.stdout.write(self.style.SUCCESS(f'Done.'))
