from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "tasks/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "tasks:login"


class RegisterView(CreateView):
    template_name = "tasks/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("tasks:login"))
