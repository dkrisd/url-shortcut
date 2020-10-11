from django import forms

from .models import Url

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class CreateUrlForm(forms.ModelForm):
    url = forms.URLField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter URL",
                "rows": 1,
                "cols": 100
            }
        )
    )
    url_shortcut = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Shortcut",
                "rows": 1,
                "cols": 30
            }
        )
    )

    class Meta:
        model = Url
        fields = [
            'url',
            'url_shortcut'
        ]