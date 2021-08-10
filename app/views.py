# from django.contrib.auth import get_user_model
import markdown
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import FileResponse

# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AnnouncementForm, EditAnnouncementForm, EditLessonForm, LessonForm
from .models import Announcement, Lesson

# Create your views here.

# def Dashboard(request):
#     all_users = get_user_model().objects.all()
#     username = request.user.username
#     page = request.GET.get("page")
#     user_list = User.objects.all()
#     paginator = Paginator(user_list, 10)
#     try:
#         all_users = paginator.page(page)
#     except PageNotAnInteger:
#         all_users = paginator.page(1)
#     except EmptyPage:
#         all_users = paginator.page(paginator.num_pages)
#     group_list = []
#     user_groups = request.user.groups.all()
#     for group in user_groups:
#         group_list.append(group.name)
#     formatted_group_list = ", ".join(str(group) for group in group_list)
#     return render(
#         request,
#         "admin/dashboard.html",
#         {
#             "loggedin_username": username,
#             "all_users": all_users,
#             "current_groups": formatted_group_list,
#         },
#     )


class HomeView(ListView):
    model = Announcement
    template_name = "pages/home.html"
    paginate_by = 5
    query_set = Announcement.objects.all()
    context_object_name = "announcements"
    ordering = ["-announcement_date"]


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/announcement.html"


class AddAnnouncementView(SuccessMessageMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcements/add_announcement.html"
    success_message = "Your announcement was posted successfully"


class UpdateAnnouncementView(SuccessMessageMixin, UpdateView):
    model = Announcement
    template_name = "announcements/update_announcement.html"
    form_class = EditAnnouncementForm
    success_message = "Your announcement was updated successfully"


class DeleteAnnouncementView(SuccessMessageMixin, DeleteView):
    model = Announcement
    template_name = "announcements/delete_announcement.html"

    def get_success_url(self):
        messages.success(self.request, "The announcement was successfully deleted")
        return reverse("home")


@login_required()
def LessonLandingPage(request):
    return render(request, "lessons/lesson_difficulty.html")


@login_required()
def LessonDisplayView(request, diff):
    diff_original = diff.capitalize()
    diff_lessons = Lesson.objects.filter(difficulty=diff_original)
    return render(
        request,
        "lessons/lesson.html",
        {"diff": diff_original, "diff_lessons": diff_lessons},
    )


class AddLessonView(SuccessMessageMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "lessons/add_lesson.html"
    success_message = "Your lessons was posted successfully"


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = "lessons/lesson_detail_view.html"


class UpdateLessonView(SuccessMessageMixin, UpdateView):
    model = Lesson
    template_name = "lessons/update_lesson.html"
    form_class = EditLessonForm
    success_message = "The lesson was updated successfully"


class DeleteLessonView(SuccessMessageMixin, DeleteView):
    model = Lesson
    template_name = "lessons/delete_lesson.html"

    def get_success_url(self):
        messages.success(self.request, "The lesson was successfully deleted")
        return reverse("home")


@login_required()
def events_page(request):
    return render(request, "pages/events.html")


def about_page(request):
    return render(request, "pages/about.html")


def terms_of_service(request):
    terms_of_service_content = ""
    with open("app/templates/pages/markdown/tos.md") as f:
        terms_of_service_markdown = f.read()
        parsed_markdown = markdown.markdown(terms_of_service_markdown)
        terms_of_service_content = parsed_markdown
    return render(request, "pages/tos.html", {"content": terms_of_service_content})


def terms_pdf(request):
    pdf = open("staticfiles/terms-of-service.pdf", "rb")
    response = FileResponse(pdf)
    return response


def privacy_policy(request):
    privacy_policy_content = ""
    with open("app/templates/pages/markdown/privacypolicy.md") as f:
        privacy_policy_markdown = f.read()
        parsed_markdown = markdown.markdown(privacy_policy_markdown)
        privacy_policy_content = parsed_markdown
    return render(
        request, "pages/privacypolicy.html", {"content": privacy_policy_content}
    )


def privacy_pdf(request):
    pdf = open("staticfiles/privacy-policy.pdf", "rb")
    response = FileResponse(pdf)
    return response
