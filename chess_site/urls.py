from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("members/", include("members.urls")),
    path("comment/", include("comment.urls")),
    path("martor/", include("martor.urls")),
]
