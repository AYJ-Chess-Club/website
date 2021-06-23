from django.urls import path
from . import views
from .views import ShowProfileView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("confirm-account/<uidb64>/<token>/", views.activate, name="confirm-account"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.view_profile, name="profile"),
    path(
        "profile/<str:username>/view/", ShowProfileView.as_view(), name="show-profile"
    ),
    path("users/all/", views.all_users_view, name="all-users"),
    path(
        "profile/edit/", views.edit_profile_view, name="edit-profile"
    ),
]
