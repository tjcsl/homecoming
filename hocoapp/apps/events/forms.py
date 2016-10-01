import bleach

from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):

    """A Form to create an Event"""

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

    def clean_description(self):
        data = self.cleaned_data['description']
        return bleach.clean(data,
            tags=['a', 'b', 'strong', 'img', 'table', 'thead', 'tbody', 'th', 'tr', 'td', 'hr', 'b', 'i', 'u', 's', 'sup', 'sub', 'p', 'ul', 'ol', 'li', 'em', 'blockquote'],
            attributes={
                '*': ['title'],
                'a': ['href'],
                'img': ['src', 'alt']
            }
        )

    description = forms.CharField(widget=forms.Textarea)
    start_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}))
    end_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S"], widget=forms.DateTimeInput(attrs={"class": "datetimepicker"}))

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "start_time",
            "end_time"
        ]
