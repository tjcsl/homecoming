import datetime

from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=48000)
    location = models.CharField(max_length=512)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        location: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
    ):  # pylint: disable=too-many-arguments
        event = cls(
            name=name,
            description=description,
            location=location,
            start_time=start_time,
            end_time=end_time,
        )
        event.save()
        return event

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("start_time",)
