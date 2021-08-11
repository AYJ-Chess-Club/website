from app.utils.identicon import getIdenticon
from django.contrib.auth.decorators import login_required
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.detail import DetailView
from .forms import EditProfileForm, RegisterForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .lichess_api import (
    get_blitz_rating,
    get_bullet_rating,
    get_classical_rating,
    get_rapid_rating,
)

UserModel = get_user_model()


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        try:
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
            return redirect("login")
        except Exception as e:
            messages.error(
                request,
                f"Please ensure that all credentials were filled in properly. Error: {e}",
            )
            return redirect("register")

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
        next_request = request.POST.get("next")
        if user is not None:
            login(request, user)
            if next_request:
                messages.success(request, "Successfully logged in.")
                return redirect(next_request)
            else:
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


def forgot_password(request):
    if request.method == "POST":
        current_site = get_current_site(request)
        _username = request.POST.get("_username")
        _email = request.POST.get("_email")
        user = User.objects.get(username__exact=_username)
        if _username and _email:
            try:
                mail_subject = "AYJ Chess Club password reset"
                message = render_to_string(
                    "reset_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                    },
                )
                email = EmailMessage(mail_subject, message, to=[_email])
                email.content_subtype = "html"
                email.send()
                messages.success(
                    request,
                    "An email has been sent to your account's email. Further instructions have been included.",
                )
                return redirect("forgot-password")
            except Exception as e:
                messages.success(
                    request,
                    f"Error: {e}",
                )
                return redirect("forgot-password")

    else:
        return render(request, "password_reset.html")
    return render(request, "password_reset.html")


def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password = request.POST.get("_password")
            new_password_confirm = request.POST.get("_confirm_password")
            if new_password == new_password_confirm:
                user.set_password(new_password_confirm)
                user.save()
                messages.success(request, "Your password was successfully reset.")
                return redirect("login")
    else:
        messages.error(request, "Sorry, that reset link is invalid!")
        return redirect("home")
    context = {"uidb64": uidb64, "token": token}
    return render(request, "reset_form.html", context)


@login_required()
def change_password(request):
    if request.method == "POST":
        user = request.user
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")

        is_valid_password = user.check_password(current_password)

        if is_valid_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect("home")
        else:
            messages.error(
                request,
                "Your input does not match your current password. Please try again.",
            )
            return redirect("change-password")

    return render(request, "change_password.html")


@login_required()
def view_profile(request):
    identicon_data = requests.get(
        f"https://yakfumblepack.pythonanywhere.com/api/v0.1.0/b64/{request.user}"
    ).text

    bullet_rating = ""
    blitz_rating = ""
    rapid_rating = ""
    classical_rating = ""

    lichess_username = str(request.user.userprofile.user_lichess_username)

    try:
        bullet_rating = get_bullet_rating(lichess_username)
        blitz_rating = get_blitz_rating(lichess_username)
        rapid_rating = get_rapid_rating(lichess_username)
        classical_rating = get_classical_rating(lichess_username)
    except Exception:
        pass

    args = {
        "user": request.user,
        "identicon_data": identicon_data,
        "lichess_bullet": bullet_rating,
        "lichess_blitz": blitz_rating,
        "lichess_rapid": rapid_rating,
        "lichess_classic": classical_rating,
    }
    return render(request, "profile.html", args)


class ShowProfileView(DetailView):
    model = UserProfile
    template_name = "profile.html"

    def get_object(self):
        username_object = get_object_or_404(User, username=self.kwargs.get("username"))
        return username_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username_object = get_object_or_404(User, username=self.kwargs.get("username"))
        identicon_data = getIdenticon("b64", str(username_object))
        context["identicon_data"] = identicon_data
        return context


@login_required()
def edit_profile_view(request):
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect("profile")
        else:
            messages.error(
                request,
                "Please ensure that the CFC and FIDE rating is filled out properly.",
            )
            return redirect("edit-profile")

    else:
        profile_form = EditProfileForm(instance=request.user.userprofile)

    context = {"form": profile_form}
    return render(request, "edit_profile.html", context)


def all_users_view(request):
    all_users = get_user_model().objects.all()
    username = request.user.username
    page = request.GET.get("page")
    user_list = User.objects.all()
    paginator = Paginator(user_list, 25)
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
        "all_users.html",
        {
            "loggedin_username": username,
            "all_users": all_users,
            "current_groups": formatted_group_list,
        },
    )
