from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import addAnnouncement

# Create your views here.


class HomeView(ListView):
    model = addAnnouncement
    template_name = "pages/home.html"
    paginate_by = 5
    queryset = addAnnouncement.objects.all()
    context_object_name = "announcements"
    ordering = ["-announcement_date"]


class AnnouncementDetailView(DetailView):
    model = addAnnouncement
    template_name = "pages/announcement.html"
