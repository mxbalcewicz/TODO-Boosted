from enum import Enum

from todo.models import Task, TaskBoard, TaskCategory


class TODOAbstractFilterContextClass:
    table_headers = None
    field_list = None
    create_view = None
    detail_view = None
    create_button_name = None


class TaskCategoryFilterContext(TODOAbstractFilterContextClass):
    table_headers = ("ID", "Name", "HEX Color", "Actions")
    field_list = ("pk", "name", "color")

    create_view = "todo:category_create"
    detail_view = "todo:category_detail"

    create_button_name = "Create new category"

    @staticmethod
    def get_filters(user):
        return {"user": user}


class TaskFilterContext(TODOAbstractFilterContextClass):
    table_headers = ("ID", "Name", "Description", "Category", "Create date", "Actions")
    field_list = ("pk", "name", "description", "category", "created_at")

    create_view = "todo:task_create"
    detail_view = "todo:task_detail"

    create_button_name = "Create new task"

    @staticmethod
    def get_filters(user):
        return {"category__user": user}


class TaskBoardFilterContext(TODOAbstractFilterContextClass):
    table_headers = ("ID", "Name", "Tasks", "Create date", "Actions")
    field_list = ("pk", "name", "tasks_count", "created_at")

    create_view = "todo:board_create"
    detail_view = "todo:board_detail"

    create_button_name = "Create new board"

    @staticmethod
    def get_filters(user):
        return {"owner": user}


class ContextEnum(Enum):
    CATEGORY = TaskCategoryFilterContext
    TASK = TaskFilterContext
    BOARD = TaskBoardFilterContext

    @staticmethod
    def get_class(model):
        return {
            Task: ContextEnum.TASK.value,
            TaskCategory: ContextEnum.CATEGORY.value,
            TaskBoard: ContextEnum.BOARD.value,
        }[model]
