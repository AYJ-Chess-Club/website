from django.urls import path
from . import views
from .views import ShowProfileView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("confirm-account/<uidb64>/<token>/", views.activate, name="confirm-account"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.view_profile, name="profile"),
    path("profile/<str:username>/", ShowProfileView.as_view(), name="show-profile"),
    path("users/all/", views.all_users_view, name="all-users"),
    path("profile/edit/", views.edit_profile_view, name="edit-profile"),
    path("forgot-password/", views.forgot_password, name="forgot-password"),
    path(
        "confirm-password/<uidb64>/<token>",
        views.reset_password_confirm,
        name="reset-password-confirm",
    ),
    path("change-password/", views.change_password, name="change-password"),
]
