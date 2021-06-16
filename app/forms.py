from django import forms
from .models import addAnnouncement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = addAnnouncement
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditAnnouncementForm(forms.ModelForm):
    class Meta:
        model = addAnnouncement
        fields = ("title", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
