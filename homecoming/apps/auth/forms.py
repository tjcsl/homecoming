import bleach

from django import forms
from django.core.exceptions import ValidationError

from .models import ClassGroup


class ClassGroupForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ClassGroup
        fields = ["name", "username_prefix", "message"]

    def clean_message(self):
        data = self.cleaned_data["message"]
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
                "iframe": [
                    "allowfullscreen",
                    "mozallowfullscreen",
                    "frameborder",
                    "src",
                    "tabindex",
                    "webkitallowfullscreen",
                ],
            },
        )
