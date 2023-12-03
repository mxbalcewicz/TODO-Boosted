from accounts.models import User
from django.views.generic import ListView


class UsersManagementListView(ListView):
    template_name = "management_users_list.html"
    view_name = "users_management_list_view"
    model = User
    queryset = User.objects.all()
    context_object_name = "users"
