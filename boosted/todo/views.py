from django.views.generic import TemplateView
from tools.views import BoostedAbstractView


class TODOGenericView(BoostedAbstractView):
    app_name = "todo"


class TODOBaseView(TODOGenericView, TemplateView):
    view_name = "todo_base"
    template_name = "todo_base.html"


class TODOManagementView(TODOGenericView):
    view_name = "todo_management"
    template_name = "todo_management.html"


class TODOBoardListView(TODOGenericView):
    pass
