from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm
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

        print("fail1")
        print(form.errors)
        if form.is_valid():
            print("fail2")
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
            email.send()
            messages.success(
                request,
                "Your account was created, please check your email to activate it.",
            )
            print("success")
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
        return render(request, "login.html")
    else:
        messages.error(request, "Sorry, that activation link is invalid!")
        return render(request, "register.html")


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