from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from comment.models import Comment


class lessonDifficulty(models.Model):
    difficulty = models.CharField(max_length=225)

    def __str__(self):
        return self.difficulty

    def get_absolute_url(self):
        return reverse("home")


class Announcement(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    announcement_date = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title + "-" + str(self.announcement_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("home")


class Lesson(models.Model):

    difficulty_levels = lessonDifficulty.objects.all().values_list(
        "difficulty", "difficulty"
    )

    difficulty_levels_list = []

    for difficulty in difficulty_levels:
        difficulty_levels_list.append(difficulty)

    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=225, choices=difficulty_levels)
    body = RichTextField(blank=True, null=True)
    lesson_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "-" + str(self.lesson_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
