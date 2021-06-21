from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_profile_pic = CharField(max_length=10000, blank=True)
    user_cfc_rating = IntegerField(default=None, validators=[MinValueValidator(0), MaxValueValidator(3500)])
    user_fide_rating = IntegerField(default=None, validators=[MinValueValidator(0), MaxValueValidator(3500)])
    user_website_username = CharField(max_length=10000, blank=True)
    user_github_username = CharField(max_length=10000, blank=True)
    user_lichess_username = CharField(max_length=10000, blank=True)
    user_instagram_username = CharField(max_length=10000, blank=True)
    user_facebook_username = CharField(max_length=10000, blank=True)
    user_discord_username = CharField(max_length=10000, blank=True)
    user_bio = RichTextField(blank=True)

    def __str__(self):
        return str(self.user)
