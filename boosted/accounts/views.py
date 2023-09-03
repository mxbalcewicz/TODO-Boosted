from typing import Any, Dict

from accounts.forms import UserCreationForm
from accounts.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import FormView


class BoostedLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("dashboard")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super(RegisterView, self).get_context_data(**kwargs)
        context_data["users"] = User.objects.all()
        return context_data
