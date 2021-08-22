from django import forms
from .models import Announcement, Lesson, Tournament, lessonDifficulty


difficulty_levels = lessonDifficulty.objects.all().values_list(
    "difficulty", "difficulty"
)

difficulty_levels_list = []

for difficulty in difficulty_levels:
    difficulty_levels_list.append(difficulty)


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "author_field",
                    "value": "",
                    "type": "hidden",
                }
            ),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "author", "difficulty", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "author_field",
                    "value": "",
                    "type": "hidden",
                }
            ),
            "difficulty": forms.Select(
                choices=difficulty_levels, attrs={"class": "form-select"}
            ),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = (
            "tournament_name",
            "tournament_date",
            "tournament_link",
            "tournament_description",
        )

        widgets = {
            "tournament_name": forms.TextInput(attrs={"class": "form-control"}),
            "tournament_date": forms.TextInput(attrs={"class": "form-control"}),
            "tournament_link": forms.TextInput(attrs={"class": "form-control"}),
            "tournament_description": forms.Textarea(attrs={"class": "form-control"}),
        }
