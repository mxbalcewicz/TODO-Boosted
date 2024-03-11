from enum import Enum

from todo.models import Task, TaskCategory


class TODOAbstractFilterContextClass:
    create_view_name = None
    detail_view_name = None
    delete_view_name = None


class TaskCategoryFilterContext(TODOAbstractFilterContextClass):
    table_headers = ["ID", "Name", "HEX Color", "Actions"]
    field_list = ("pk", "name", "color")
    create_button_name = "Create new category"

    @staticmethod
    def get_filters(user):
        return {"user": user}


class TaskFilterContext(TODOAbstractFilterContextClass):
    table_headers = ["ID", "Name", "Description", "Create date", "Actions"]
    field_list = ("pk", "name", "description", "category__name", "created_at")
    create_button_name = "Create new task"

    @staticmethod
    def get_filters(user):
        return {"category__user": user}


class TaskBoardFilterContext(TODOAbstractFilterContextClass):
    @staticmethod
    def get_filters(user):
        return {"owner": user}


class ContextEnum(Enum):
    CATEGORY = TaskCategoryFilterContext
    TASK = TaskFilterContext

    @staticmethod
    def get_class(model):
        return {Task: ContextEnum.TASK.value, TaskCategory: ContextEnum.CATEGORY.value}[
            model
        ]
