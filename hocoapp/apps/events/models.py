from django.db import models

# Create your models here.


class Event(models.Model):

    """A Model for an Event in Homecoming Week"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    time = models.DateTimeField()

    @classmethod
    def create(cls, name=None, description=None, time=None):
        event = cls(name=name, description=description, time=time)
        return event
