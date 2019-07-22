from django.db.models import Q

from notes.cashback.models import Log


def get_referer(log):
    logs = Log.objects.filter(
        client_id=log.client_id,
        date__lt=log.date,
    ).order_by('-date')
    referer = None
    for log in logs:
        if log.document_location.endswith('checkout'):
            break
        if '.theirs' in log.document_referer:
            referer = None
            break
        if 'referal.ours.com' in log.document_referer:
            referer = log.document_referer
            break
    return referer
