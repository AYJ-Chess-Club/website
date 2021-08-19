from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from martor.models import MartorField
from django.db.models.signals import post_save
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_profile_pic = CharField(max_length=10000, blank=True)
    user_cfc_rating = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3500)],
        null=True,
    )
    user_fide_rating = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3500)],
        null=True,
    )
    user_website_username = CharField(max_length=10000, blank=True)
    user_github_username = CharField(max_length=10000, blank=True)
    user_lichess_username = CharField(max_length=10000, blank=True)
    user_instagram_username = CharField(max_length=10000, blank=True)
    user_facebook_username = CharField(max_length=10000, blank=True)
    user_discord_username = CharField(max_length=10000, blank=True)
    user_bio = MartorField(blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("show-profile", kwargs={"username": self.user.username})


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
