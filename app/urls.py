from django.urls import path
from .views import (
    DeleteTournamentView,
    HomeView,
    AnnouncementDetailView,
    LessonDetailView,
    LessonDisplayView,
    LessonLandingPage,
    TournamentDetailView,
    TournamentListView,
    UpdateTournamentView,
    events_page,
    about_page,
    UpdateAnnouncementView,
    AddLessonView,
    UpdateLessonView,
    DeleteAnnouncementView,
    DeleteLessonView,
    privacy_pdf,
    privacy_policy,
    terms_of_service,
    terms_pdf,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "announcements/<int:pk>/",
        AnnouncementDetailView.as_view(),
        name="announcement-detail-page",
    ),
    path(
        "admin/app/announcement/<int:pk>/change/",
        UpdateAnnouncementView.as_view(),
        name="update-announcement",
    ),
    path(
        "admins/announcements/<int:pk>/delete/",
        DeleteAnnouncementView.as_view(),
        name="delete-announcement",
    ),
    path("admin/app/lesson/add/", AddLessonView.as_view(), name="add-lesson"),
    path("difficulty/<str:diff>/", LessonDisplayView, name="difficulty-page"),
    path("lessons/", LessonLandingPage, name="lesson-page"),
    path("lessons/<int:pk>", LessonDetailView.as_view(), name="lesson-detail-page"),
    path(
        "admin/app/lesson/<int:pk>/change/",
        UpdateLessonView.as_view(),
        name="update-lesson",
    ),
    path(
        "admins/lessons/<int:pk>/delete/",
        DeleteLessonView.as_view(),
        name="delete-lesson",
    ),
    path("events/", events_page, name="events-page"),
    path("about/", about_page, name="about-page"),
    path("terms-of-service/", terms_of_service, name="terms-of-service"),
    path("privacy-policy/", privacy_policy, name="privacy-policy"),
    path("pdf/terms-of-service/", terms_pdf, name="pdf-tos"),
    path("pdf/privacy-policy/", privacy_pdf, name="pdf-privacy"),
    path(
        "tournaments/<int:pk>/",
        TournamentDetailView.as_view(),
        name="tournament-detail-page",
    ),
    path(
        "admin/app/tournament/<int:pk>/change/",
        UpdateTournamentView.as_view(),
        name="update-tournament",
    ),
    path(
        "tournament/<int:pk>/delete/",
        DeleteTournamentView.as_view(),
        name="delete-tournament",
    ),
    path(
        "past-tournaments/", TournamentListView.as_view(), name="archived-tournaments"
    ),
]
