from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

# from django.db.models.query import QuerySet


class UserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


# class UserManager(models.Manager):
#     def get_queryset(self) -> QuerySet:
#         return UserQuerySet(self.model, using=self._db)

#     def active(self):
#         return self.get_queryset().active()


class User(AbstractBaseUser):
    # User data
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True, max_length=64)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=False)

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
