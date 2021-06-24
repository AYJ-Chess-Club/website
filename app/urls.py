from django.urls import path
from . import views
from .views import (
    HomeView,
    AnnouncementDetailView,
    AddAnnouncementView,
    LessonDetailView,
    LessonDisplayView,
    LessonLandingPage,
    events_page,
    UpdateAnnouncementView,
    AddLessonView,
    UpdateLessonView,
    DeleteAnnouncementView,
    DeleteLessonView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admins/dashboard/", views.Dashboard, name="admin-dashboard"),
    path(
        "announcements/<int:pk>",
        AnnouncementDetailView.as_view(),
        name="announcement-detail-page",
    ),
    path(
        "admins/add-announcement/",
        AddAnnouncementView.as_view(),
        name="add-announcement",
    ),
    path(
        "admins/announcements/edit/<int:pk>",
        UpdateAnnouncementView.as_view(),
        name="update-announcement",
    ),
    path(
        "admins/announcements/<int:pk>/delete",
        DeleteAnnouncementView.as_view(),
        name="delete-announcement",
    ),
    path("admins/add-lessons/", AddLessonView.as_view(), name="add-lesson"),
    path("difficulty/<str:diff>/", LessonDisplayView, name="difficulty-page"),
    path("lessons/", LessonLandingPage, name="lesson-page"),
    path("lessons/<int:pk>", LessonDetailView.as_view(), name="lesson-detail-page"),
    path(
        "admins/lessons/edit/<int:pk>", UpdateLessonView.as_view(), name="update-lesson"
    ),
    path(
        "admins/lessons/<int:pk>/delete",
        DeleteLessonView.as_view(),
        name="delete-lesson",
    ),
    path("events/", events_page, name="events-page"),
]
