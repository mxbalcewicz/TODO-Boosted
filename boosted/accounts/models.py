from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    # User data
    username = models.CharField()
    email = models.CharField()
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=False)

    # User activity
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # User permissions
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
