from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("confirm-account/<uidb64>/<token>/", views.activate, name="confirm-account"),
    path("login/", views.login_request, name="login")
]
