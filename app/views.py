from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import addAnnouncement
from django.contrib.auth.models import User
from .forms import AnnouncementForm, EditAnnouncementForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def Dashboard(request):
    all_users = get_user_model().objects.all()
    username = request.user.username
    page = request.GET.get("page")
    user_list = User.objects.all()
    paginator = Paginator(user_list, 10)
    try:
        all_users = paginator.page(page)
    except PageNotAnInteger:
        all_users = paginator.page(1)
    except EmptyPage:
        all_users = paginator.page(paginator.num_pages)
    group_list = []
    user_groups = request.user.groups.all()
    for group in user_groups:
        group_list.append(group.name)
    formatted_group_list = ", ".join(str(group) for group in group_list)
    return render(
        request,
        "admin/dashboard.html",
        {
            "loggedin_username": username,
            "all_users": all_users,
            "current_groups": formatted_group_list,
        },
    )


class HomeView(ListView):
    model = addAnnouncement
    template_name = "pages/home.html"
    paginate_by = 5
    query_set = addAnnouncement.objects.all()
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
    template_name = "announcements/update_announcement.html"
    form_class = EditAnnouncementForm
    success_message = "Your announcement was updated successfully"
