from django.db import models

from ..auth.models import ClassGroup


class Announcement(models.Model):

    name = models.CharField(max_length=128)
    class_group = models.ForeignKey(
        ClassGroup, on_delete=models.CASCADE, related_name="announcements"
    )
    description = models.TextField(max_length=48000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("start_time",)
