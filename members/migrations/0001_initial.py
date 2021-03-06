# Generated by Django 3.2.4 on 2021-08-07 21:07

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_profile_pic", models.CharField(blank=True, max_length=10000)),
                (
                    "user_cfc_rating",
                    models.IntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(3500),
                        ],
                    ),
                ),
                (
                    "user_fide_rating",
                    models.IntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(3500),
                        ],
                    ),
                ),
                (
                    "user_website_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                (
                    "user_github_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                (
                    "user_lichess_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                (
                    "user_instagram_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                (
                    "user_facebook_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                (
                    "user_discord_username",
                    models.CharField(blank=True, max_length=10000),
                ),
                ("user_bio", ckeditor.fields.RichTextField(blank=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
