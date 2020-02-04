from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'sign_up.html'


class SignupUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'update_user_info.html'
