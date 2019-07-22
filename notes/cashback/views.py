import json
from django.core import serializers
from django.http import HttpResponse

from notes.cashback.models import Log
from notes.cashback.utils import get_referer


def logs(request):
    logs = serializers.serialize("json", Log.objects.all())
    return HttpResponse(logs, content_type='application/json')


def cashback(request):
    results = []
    success_logs = Log.objects.filter(document_location__endswith='checkout')
    for item in success_logs:
        results.append(
            {
                'log': serializers.serialize("json", [item, ]),
                'referer': get_referer(item),
            }
        )

    return HttpResponse(results , content_type='application/json')
