from accounts.forms import UserCreationForm, UserSettingsForm
from accounts.models import User, BoostedGroup
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, UpdateView, View, ListView
from tools.views import BoostedAbstractView


class AccountsGenericView(BoostedAbstractView):
    app_name = "accounts"


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        return None


class BoostedLoginView(BoostedAbstractView, LoginView):
    view_name = "login"
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        if self.request.user.is_authenticated:
            # Redirect authenticated users to the dashboard
            from dashboard.views import DashboardView

            return reverse(DashboardView.get_view_name())
        else:
            # If the user is not authenticated, redirect to some other page or URL
            return reverse(self.view_name)

    def form_invalid(self, form):
        for err in form.error_messages.values():
            messages.error(self.request, err)
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
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(BoostedLoginView.view_name)
        return super().dispatch(*args, **kwargs)


class LogoutView(View):
    view_name = "logout"

    def get(self, request, *args, **kwargs):
        logout(request=request)
        return redirect(BoostedLoginView.view_name)


class SettingsView(AccountsGenericView, DetailView):
    view_name = "settings"
    template_name = "settings.html"
    model = User
    queryset = User.objects.all()


class SettingsEditView(AccountsGenericView, UpdateView):
    view_name = "settings_edit"
    template_name = "settings_edit.html"
    form_class = UserSettingsForm
    queryset = User.objects.all()


class UsersManagementListView(ListView):
    template_name = "management_users_list.html"
    view_name = "users_management_list_view"
    model = User
    queryset = User.objects.all()
    context_object_name = "users"


class GroupsManagementListView(ListView):
    template_name = "management_groups_list.html"
    view_name = "groups_management_list_view"
    model = BoostedGroup
    queryset = BoostedGroup.objects.all()
    context_object_name = "groups"