# Generated by Django 3.2.4 on 2021-08-09 19:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="addAnnouncement",
            new_name="Announcement",
        ),
    ]
