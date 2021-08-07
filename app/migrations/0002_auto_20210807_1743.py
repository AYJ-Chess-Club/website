# Generated by Django 3.2.4 on 2021-08-07 21:43

from django.conf import settings
from django.db import migrations, models


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
        migrations.AlterField(
            model_name="lesson",
            name="difficulty",
            field=models.CharField(
                choices=[
                    ("Beginner", "Beginner"),
                    ("Intermediate", "Intermediate"),
                    ("Advanced", "Advanced"),
                ],
                max_length=225,
            ),
        ),
    ]
