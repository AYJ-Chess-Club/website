from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import addAnnouncement, addLesson
from django.contrib.auth.models import User
from .forms import AnnouncementForm, EditAnnouncementForm, LessonForm, EditLessonForm
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

def LessonLandingPage(request):
     return render(request, "lessons/lesson_difficulty.html")

def LessonDisplayView(request, diff):
    diff_original = diff.capitalize()
    diff_lessons = addLesson.objects.filter(difficulty=diff_original)
    print(diff_lessons)
    return render(request, "lessons/lesson.html", {"diff": diff_original, "diff_lessons": diff_lessons})

class AddLessonView(SuccessMessageMixin, CreateView):
    model = addLesson
    form_class = LessonForm
    template_name = "lessons/add_lesson.html"
    success_message = "Your lessons was posted successfully"

class LessonDetailView(DetailView):
    model = addLesson
    template_name = "lessons/lesson_detail_view.html"

class UpdateLessonView(SuccessMessageMixin, UpdateView):
    model = addLesson
    template_name = "lessons/update_lesson.html"
    form_class = EditLessonForm
    success_message = "The lesson was updated successfully"