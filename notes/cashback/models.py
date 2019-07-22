from django.db import models


class Log(models.Model):
    client_id = models.CharField('Client ID', max_length=50)
    user_agent = models.CharField('User-Agent', max_length=50)
    document_location = models.CharField('Referer', max_length=256)
    document_referer = models.CharField('Referer', max_length=256)
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __str__(self) -> str:
        return f'[{self.client_id}] {self.date}'
