from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class lessonDifficulty(models.Model):
    difficulty = models.CharField(max_length=225)

    def __str__(self):
        return self.difficulty

    def get_absolute_url(self):
        return reverse("home")
    

class addAnnouncement(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    announcement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "-" + str(self.announcement_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

class addLesson(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=225, default="Easy")
    body = RichTextField(blank=True, null=True)
    lesson_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "-" + str(self.lesson_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
