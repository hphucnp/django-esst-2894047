from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/signup.html"
    success_url = reverse_lazy("login")


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"
    next_page = "/"
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.next_page)
