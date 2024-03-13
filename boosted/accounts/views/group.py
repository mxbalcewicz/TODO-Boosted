from accounts.forms import BoostedGroupForm
from accounts.models import BoostedGroup
from accounts.views import AccountsGenericView
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from tools.views import GenericCreateView


@method_decorator(permission_required("accounts.view_boostedgroup"), name="dispatch")
class GroupsManagementListView(ListView, AccountsGenericView):
    template_name = "group_list.html"
    view_name = "group_list"
    model = BoostedGroup
    queryset = BoostedGroup.objects.all()
    context_object_name = "groups"


@method_decorator(permission_required("accounts.change_boostedgroup"), name="dispatch")
class GroupDetailView(DetailView, AccountsGenericView):
    view_name = "group_detail"
    template_name = "group_detail.html"
    model = BoostedGroup
    context_object_name = "group"


@method_decorator(permission_required("accounts.change_boostedgroup"), name="dispatch")
class GroupUpdateView(UpdateView, AccountsGenericView):
    view_name = "group_update"
    model = BoostedGroup
    form_class = BoostedGroupForm
    template_name = "group_update.html"
    context_object_name = "group"

    def get_success_url(self) -> str:
        return reverse(GroupDetailView.get_view_name(), args=[self.object.pk])


@method_decorator(permission_required("accounts.change_boostedgroup"), name="dispatch")
class GroupDeleteView(DeleteView, AccountsGenericView):
    view_name = "group_delete"
    model = BoostedGroup

    def get_success_url(self) -> str:
        return reverse(GroupsManagementListView.get_view_name())


@method_decorator(permission_required("accounts.change_boostedgroup"), name="dispatch")
class GroupCreateView(GenericCreateView, AccountsGenericView):
    view_name = "group_create"
    model = BoostedGroup
    form_class = BoostedGroupForm
    form_title = "New group"
    back_url = "accounts:group_list"

    def get_success_url(self) -> str:
        return reverse(GroupDetailView.get_view_name(), args=[self.object.pk])
