import bleach

from django import forms
from django.core.exceptions import ValidationError

from ..forms import bleach_clean
from .models import Event


class CreateEventForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)
    start_time = forms.DateTimeField(
        input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}),
    )
    end_time = forms.DateTimeField(
        input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}),
    )

    class Meta:
        model = Event
        fields = ["name", "description", "location", "start_time", "end_time"]

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data["start_time"] > cleaned_data["end_time"]:
            raise ValidationError("Start time cannot be after end time!")

    def clean_description(self):
        return bleach_clean(self.cleaned_data["description"])
