from django.urls import path
from . import views
from .views import ShowProfileView, EditProfileView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("confirm-account/<uidb64>/<token>/", views.activate, name="confirm-account"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("<str:username>/profile/", ShowProfileView.as_view(), name="profile"),
    path(
        "profile/<str:username>/edit/", EditProfileView.as_view(), name="edit-profile"
    ),
]
