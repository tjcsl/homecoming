from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):

    """A Form to create an Event"""

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

    time = forms.DateTimeInput()

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "time"
        ]
