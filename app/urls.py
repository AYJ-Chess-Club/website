from django.urls import path

# from . import views
from .views import HomeView, AnnouncementDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "announcements/<int:pk>",
        AnnouncementDetailView.as_view(),
        name="announcement-detail-page",
    ),
]
