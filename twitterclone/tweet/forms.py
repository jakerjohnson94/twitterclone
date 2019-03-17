from django import forms
from .models import Tweet


class PostTweetForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(), max_length=140)

    class Meta:
        model = Tweet
        fields = {"body"}
        exclude = ["sender_id"]

