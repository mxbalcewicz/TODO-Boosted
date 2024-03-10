from django.db import models
from django.urls import reverse


class AppLabel(models.Model):
    label = models.CharField(unique=True)
    view_name = models.CharField()
    app_name = models.CharField()

    def get_app_url(self):
        return reverse(f"{self.app_name}:{self.view_name}")
