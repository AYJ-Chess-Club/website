from django.urls import path
from . import views
from .views import HomeView, AnnouncementDetailView, AddAnnouncementView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "announcements/<int:pk>",
        AnnouncementDetailView.as_view(),
        name="announcement-detail-page",
    ),
    path("add-announcement/", AddAnnouncementView.as_view(), name="add-announcement")
]
