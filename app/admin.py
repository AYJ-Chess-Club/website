from django.contrib import admin
from .models import Announcement, Lesson, Tournament, lessonDifficulty


class LessonAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "difficulty",
        "body",
    ]

    fields = ("title", "difficulty", "body")

    def save_model(self, request, obj, *args, **kwargs):
        if getattr(obj, "author", None) is None:
            obj.author = request.user

        obj.save()


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "body"]

    fields = ("title", "body")

    def save_model(self, request, obj, *args, **kwargs):
        if getattr(obj, "author", None) is None:
            obj.author = request.user

        obj.save()


class TournamentAdmin(admin.ModelAdmin):
    list_display = ["tournament_name", "tournament_date", "author", "tournament_link", "tournament_description"]

    fields = ("tournament_name", "tournament_date", "tournament_link", "tournament_description")

    def save_model(self, request, obj, *args, **kwargs):
        if getattr(obj, "author", None) is None:
            obj.author = request.user

        obj.save()

# Register your models here.
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(lessonDifficulty)
admin.site.register(Lesson, LessonAdmin)
