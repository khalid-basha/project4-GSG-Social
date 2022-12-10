from django.urls import path, include
from .views import dashboard, profile_list, profile, redirect_view, register

#app_name = "dwitter"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('redirect/', redirect_view),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
