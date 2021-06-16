from django.db import models
from django.conf import settings as config_settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

class addAnnouncement(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    announcement_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + "-" + str(self.announcement_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("announcement-detail-page", kwargs={"pk": self.pk})
    