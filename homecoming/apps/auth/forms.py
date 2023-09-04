import bleach

from django import forms

from ..forms import bleach_clean
from .models import ClassGroup


class ClassGroupForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ClassGroup
        fields = ["name", "username_prefix", "message"]

    def clean_message(self):
        return bleach_clean(self.cleaned_data["message"])
