from accounts.models import User
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from tools.models import HexColorField


class TaskCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    color = HexColorField()

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    history = HistoricalRecords()


class TaskBoard(models.Model):
    name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    categories = models.ManyToManyField(TaskCategory)

    @property
    def tasks_count(self):
        return self.tasks.count()

    def get_absolute_url(self):
        from todo.views import TaskBoardDetailView

        return reverse(TaskBoardDetailView.get_view_name(), kwargs={"pk": self.pk})
