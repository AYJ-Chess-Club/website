from django import forms
from members.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from martor.widgets import MartorWidget


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")


class EditProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "user_profile_pic",
            "user_cfc_rating",
            "user_fide_rating",
            "user_website_username",
            "user_github_username",
            "user_lichess_username",
            "user_instagram_username",
            "user_facebook_username",
            "user_discord_username",
            "user_bio",
        )

        labels = {
            "user_profile_pic": "Profile picture url",
            "user_cfc_rating": "CFC rating",
            "user_fide_rating": "FIDE rating",
            "user_website_username": "Your website link",
            "user_github_username": "Github username",
            "user_lichess_username": "Lichess username",
            "user_instagram_username": "Instagram username",
            "user_facebook_username": "Facebook username",
            "user_discord_username": "Discord username",
            "user_bio": "Your bio",
        }

        widgets = {
            "user_profile_pic": forms.TextInput(attrs={"class": "form-control"}),
            "user_cfc_rating": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave as 0 if not applicable",
                }
            ),
            "user_fide_rating": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave as 0 if not applicable",
                }
            ),
            "user_website_username": forms.TextInput(attrs={"class": "form-control"}),
            "user_github_username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: mojombo"}
            ),
            "user_lichess_username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: DrNykterstein"}
            ),
            "user_instagram_username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: ayjchessclub"}
            ),
            "user_facebook_username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: facebook"}
            ),
            "user_discord_username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: username#0000"}
            ),
            "user_bio": MartorWidget(),
        }
