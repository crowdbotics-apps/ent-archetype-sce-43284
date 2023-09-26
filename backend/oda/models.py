from django.conf import settings
from django.db import models
class Event(models.Model):
    'Generated Model'
    event_id = models.BigIntegerField()
    event_type = models.TextField(null=True,blank=True,)
    date_time = models.DateTimeField(null=True,blank=True,)
    severity = models.TextField(null=True,blank=True,)
    source = models.TextField(null=True,blank=True,)
    title = models.TextField(null=True,blank=True,)
    description = models.TextField(null=True,blank=True,)
    event_handler = models.TextField(null=True,blank=True,)
    disposition = models.TextField(null=True,blank=True,)

# Create your models here.
