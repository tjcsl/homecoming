import bleach

from django import forms
from django.core.exceptions import ValidationError

from .models import Event


class CreateEventForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)
    start_time = forms.DateTimeField(
        input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"})
    )
    end_time = forms.DateTimeField(
        input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"})
    )

    class Meta:
        model = Event
        fields = ["name", "description", "location", "start_time", "end_time"]

    def clean(self):
        cd = self.cleaned_data
        if cd["start_time"] > cd["end_time"]:
            raise ValidationError("Start time cannot be after end time!")

    def clean_description(self):
        data = self.cleaned_data["description"]
        return bleach.clean(
            data,
            tags=[
                "a",
                "b",
                "div",
                "iframe",
                "strong",
                "img",
                "table",
                "thead",
                "tbody",
                "th",
                "tr",
                "td",
                "hr",
                "br",
                "b",
                "i",
                "u",
                "s",
                "sup",
                "sub",
                "p",
                "ul",
                "ol",
                "li",
                "em",
                "blockquote",
            ],
            attributes={
                "*": ["title", "style"],
                "a": ["href"],
                "img": ["src", "alt"],
                "div": ["data-oembed-url"],
                "iframe": ["allowfullscreen", "mozallowfullscreen", "frameborder", "src", "tabindex", "webkitallowfullscreen"],
            },
        )
