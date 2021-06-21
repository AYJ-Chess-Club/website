from django.contrib.messages.views import SuccessMessageMixin
import requests
from members.models import UserProfile
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import EditProfileForm, RegisterForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

UserModel = get_user_model()


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "AYJ Chess Club account activation"
            message = render_to_string(
                "confirm_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.content_subtype = "html" 
            email.send()
            messages.success(
                request,
                "Your account was created, please check your email to activate it.",
            )
            return render(request, "register.html")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, "Your account was successfully activated. Please login."
        )
        return redirect("login")
    else:
        messages.error(request, "Sorry, that activation link is invalid!")
        return redirect("register")


def login_request(request):
    if request.method == "POST":
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("/")
        else:
            messages.error(
                request,
                "Please ensure all fields are filled out with the correct credentials.",
            )
            return render(request, "login.html")

    return render(request, "login.html")


def logout_request(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect("/")

class ShowProfileView(DetailView):
    model = UserProfile
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        profile_username = self.kwargs.get("username")
        current_profile_username = get_object_or_404(User, username=profile_username)
        identicon_data = requests.get(f"https://identiconapi.ayjchess.repl.co/api/v0.1.0/b64/{current_profile_username}").text
        context["identicon_data"] = identicon_data
        return context

    def get_object(self):
        profile_username = self.kwargs.get("username")
        current_profile_username = get_object_or_404(User, username=profile_username)
        return current_profile_username

class EditProfileView(SuccessMessageMixin, UpdateView):
    model = UserProfile
    template_name = "edit_profile.html"
    queryset = User.objects.all()
    form_class = EditProfileForm

    def get_object(self):
        profile_username = self.kwargs.get("username")
        current_profile_username = get_object_or_404(User, username=profile_username)
        return current_profile_username

    def return_context(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(UserProfile, id=self.kwargs["pk"])
        context["current_user"] = current_user
        return context