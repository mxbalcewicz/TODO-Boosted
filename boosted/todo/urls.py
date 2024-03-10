from django.urls import re_path
from todo.views import TODOBaseView

urlpatterns = [
    re_path(r"", TODOBaseView.as_view(), name=TODOBaseView.view_name),
]
