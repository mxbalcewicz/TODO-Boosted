from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.urls import reverse


class UserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def create_user(self, email, username, password=None):
        user = self.model(username=username, email=email, date_joined=datetime.now())

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # User data
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True, max_length=64)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    # User activity
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # User permissions
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return f"{self.username}: {self.email}"

    def get_absolute_url(self):
        from accounts.views import SettingsView

        return reverse(SettingsView.get_view_name(), kwargs={"pk": self.pk})
