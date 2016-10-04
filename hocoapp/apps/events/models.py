from django.db import models

# Create your models here.


class Event(models.Model):

    """A Model for an Event in Homecoming Week"""

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=48000)
    location = models.CharField(max_length=512)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @classmethod
    def create(cls, name, description, location, start_time, end_time):
        event = cls(name=name, description=description, location=location, start_time=start_time, end_time=end_time)
        event.save()
        return event
