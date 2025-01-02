from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import UserLoginForm
from .views import SignUpView

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
