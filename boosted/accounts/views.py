from accounts.forms import UserCreationForm, UserSettingsForm, UserUpdateForm, LoginForm
from accounts.models import User, BoostedGroup
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, UpdateView, View, ListView
from accounts.forms import GroupUpdateForm
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from accounts import AccountsGenericView









