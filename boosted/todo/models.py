from accounts.models import User
from django.db import models
from simple_history.models import HistoricalRecords
from tools.models import HexColorField


class TaskCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    color = HexColorField()


class Task(models.Model):
    name = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    history = HistoricalRecords()
