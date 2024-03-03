from accounts.forms import UserCreationForm, UserSettingsForm, LoginForm, UserUpdateForm
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, UpdateView, View, ListView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from accounts import AccountsGenericView


class SelfUserRestrictedView:
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_admin:
            if self.request.user.pk != int(kwargs.get("pk")):
                redirect(BoostedLoginView.view_name)
        return super().dispatch(*args, **kwargs)


class BoostedLoginView(LoginView):
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
        for err in form.errors.values():
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


class SettingsView(SelfUserRestrictedView, AccountsGenericView, DetailView):
    view_name = "settings"
    template_name = "settings.html"
    model = User
    queryset = User.objects.all()


class SettingsEditView(SelfUserRestrictedView, AccountsGenericView, UpdateView):
    view_name = "settings_edit"
    template_name = "settings_edit.html"
    form_class = UserSettingsForm
    queryset = User.objects.all()


@method_decorator(permission_required("accounts.view_user"), name="dispatch")
class UsersManagementListView(ListView, AccountsGenericView):
    template_name = "user_list.html"
    view_name = "user_list"
    model = User
    queryset = User.objects.all()
    ordering = ("pk",)
    context_object_name = "users"



@method_decorator(permission_required("accounts.change_user"), name="dispatch")
class UserDetailView(DetailView, AccountsGenericView):
    view_name = "user_detail"
    template_name = "user_detail.html"
    model = User
    context_object_name = "user"


@method_decorator(permission_required("accounts.change_user"), name="dispatch")
class UserUpdateView(UpdateView, AccountsGenericView):
    view_name = "user_update"
    model = User
    form_class = UserUpdateForm
    template_name = "user_update.html"
    context_object_name = "user"

    def get_success_url(self) -> str:
        return reverse(UserDetailView.get_view_name(), args=[self.object.pk])