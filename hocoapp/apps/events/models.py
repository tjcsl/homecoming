from django.db import models

# Create your models here.


class Event(models.Model):

    """A Model for an Event in Homecoming Week"""

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    time = models.DateTimeField()

    @classmethod
    def create(cls, name, description, time):
        event = cls(name=name, description=description, time=time)
        event.save()
        return event
