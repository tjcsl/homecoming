from django import forms

from .models import ScoreBoard


class EditScoresForm(forms.ModelForm):

    """A Form to create an Event"""

    class Meta:
        model = ScoreBoard
        fields = ["freshman_score", "sophomore_score", "junior_score", "senior_score"]
