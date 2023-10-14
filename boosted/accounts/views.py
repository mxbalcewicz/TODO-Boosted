from accounts.forms import UserCreationForm, UserSettingsForm
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, View
from tools.views import BoostedAbstractView


class BoostedLoginView(LoginView):
    view_name = "login"
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_authenticated:
            # Redirect authenticated users to the dashboard
            from dashboard.views import DashboardView

            return reverse(DashboardView.get_view_name())
        else:
            # If the user is not authenticated, redirect to some other page or URL
            return reverse(self.view_name)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    view_name = "register"
    form_class = UserCreationForm
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "User successfully registered")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(BoostedLoginView.view_name)


class LogoutView(View):
    view_name = "logout"

    def get(self, request, *args, **kwargs):
        logout(request=request)
        return redirect(BoostedLoginView.view_name)


class SettingsView(BoostedAbstractView, DetailView):
    view_name = "settings"
    template_name = "settings.html"
    model = User
    queryset = User.objects.active()


class SettingsEditView(BoostedAbstractView, FormView):
    view_name = "settings_edit"
    template_name = "settings_edit.html"
    form_class = UserSettingsForm
