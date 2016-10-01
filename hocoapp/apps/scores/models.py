from django.db import models

from ..events.models import Event

# Create your models here.


class ScoreBoard(models.Model):

    """A ScoreBoard keeps track of an Event.
    It has a score field for all 4 classes"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    freshman_score = models.IntegerField()
    sophomore_score = models.IntegerField()
    junior_score = models.IntegerField()
    senior_score = models.IntegerField()

    @classmethod
    def create(cls, event, freshman_score=0, sophomore_score=0, junior_score=0, senior_score=0):
        scoreboard = cls(event=event, freshman_score=freshman_score,
                         sophomore_score=sophomore_score, junior_score=junior_score, senior_score=senior_score)
        scoreboard.save()
        return scoreboard
