from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):

    """A Form to create an Event"""

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

    description = forms.CharField(widget=forms.Textarea)
    start_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}))
    end_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}))

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "start_time",
            "end_time"
        ]
