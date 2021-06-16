# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import addAnnouncement
from .forms import AnnouncementForm, EditAnnouncementForm

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
    template_name = "announcements/announcement.html"

class AddAnnouncementView(SuccessMessageMixin, CreateView):
    model = addAnnouncement
    form_class = AnnouncementForm
    template_name = "announcements/add_announcement.html"
    success_message = "Your announcement was posted successfully"

class UpdateAnnouncementView(SuccessMessageMixin, UpdateView):
    model = addAnnouncement
    template_name = 'announcements/update_announcement.html'
    form_class = EditAnnouncementForm
    success_message = "Your announcement was updated successfully"
