from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView as prdv
from django.contrib.auth.views import PasswordResetConfirmView as prcv
from django.contrib.auth.views import PasswordResetCompleteView as prcomv


app_name = "users"

urlpatterns = [
    path("signup/", views.signupuser, name="signup"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset-password/done/",
        prdv.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        prcv.as_view(
            template_name="users/password_reset_confirm.html",
            success_url="/users/reset-password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password/complete/",
        prcomv.as_view(template_name="users/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]
