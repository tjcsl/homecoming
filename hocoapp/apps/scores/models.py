from django.db import models

from ..events.models import Event

# Create your models here.


class ScoreBoard(models.Model):

    """A ScoreBoard keeps track of an Event.
    It has a score field for all 4 classes"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    freshman_score = models.DecimalField(max_digits=10, decimal_places=2)
    sophomore_score = models.DecimalField(max_digits=10, decimal_places=2)
    junior_score = models.DecimalField(max_digits=10, decimal_places=2)
    senior_score = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def create(cls, event=None, freshman_score=None, sophomore_score=None, junior_score=None, senior_score=None):
        scoreboard = cls(event=event, freshman_score=freshman_score,
                         sophomore_score=sophomore_score, junior_score=junior_score, senior_score=senior_score)
        return scoreboard
