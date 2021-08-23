# from django.contrib.auth import get_user_model
import re

from django.contrib.auth.models import User
from members.lichess_api import get_tournament_rankings
import markdown

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http.response import FileResponse

# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import EditAnnouncementForm, EditLessonForm, EditTournamentForm, LessonForm
from .models import Announcement, Lesson, Tournament


class HomeView(ListView):
    context_object_name = "home_list"
    template_name = "pages/home.html"
    queryset = Announcement.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        announcement_paginator = Paginator(Announcement.objects.all().order_by(
            "-announcement_date"
        ), self.paginate_by)
        context["announcements"] = announcement_paginator.page(context["page_obj"].number)
        try:
            context["tournament"] = Tournament.objects.latest("id")
        except:
            context["tournament"] = Tournament.objects.all().order_by("-id")
        return context


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/announcement.html"


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


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = "tournaments/tournament.html"

    def get_context_data(self, **kwargs):
        context = super(TournamentDetailView, self).get_context_data(**kwargs)
        tournament_object = get_object_or_404(Tournament, id=self.kwargs.get("pk"))
        tournament_url = str(tournament_object.tournament_link)
        tournament_arr = [] 
        tournament_arr = tournament_url.split("/")
        tournament_id = tournament_arr[-1]
        try:
            tournament_json = get_tournament_rankings(tournament_id)
            context["number_of_participants"] = str(tournament_json["nbPlayers"])
            context["minutes"] = str(tournament_json["minutes"])
            context["description"] = str(tournament_json["description"])
            context["variant"] = str(tournament_json["variant"])
            context["winner"] = str(tournament_json["standing"]["players"][0]["name"])

            participants = {}
            for i in tournament_json["standing"]["players"]:
                participants[str(i["name"])] = (i["score"])

            labels = str(participants)
            labels = labels.replace("{", "").replace("}", "")
            labels = re.sub(r'\:.\d+', "", labels)

            context["participants_ranking"] = participants
            context["labels_rankings"] = labels
            context["has_data_for_graph"] = True
        except:
            pass

        # userprofile_object = get_object_or_404(User, username=self.kwargs.get("username"))

        return context


class UpdateTournamentView(UpdateView):
    model = Tournament
    template_name = "tournaments/update_tournament.html"
    form_class = EditTournamentForm


class DeleteTournamentView(SuccessMessageMixin, DeleteView):
    model = Tournament
    template_name = "tournaments/delete_tournament.html"


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
