from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, Group, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission


class UserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

    def create_user(self, email, username, password=None):
        user = self.model(username=username, email=email, date_joined=datetime.now())

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # User data
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True, max_length=64)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    # User activity
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    delete_date = models.DateField(null=True, blank=True)

    # User permissions
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    @property
    def is_admin(self):
        if self.is_superuser:
            return True
        return self in BoostedGroup.objects.get(name="Admin").user_set.all()
    
    def get_user_groups(self):
        return " | ".join([group.name for group in self.groups.all()])
    
    def get_user_permissions(self):
        permissions = self.user_permissions.all() | Permission.objects.filter(group__user=self)
        return " | ".join([permission.name for permission in permissions])

    def has_perm(self, perm: str, obj) -> bool:
        if self.is_admin:
            return True
        return super().has_perm(perm, obj)

    def __str__(self):
        return f"{self.username}: {self.email}"

    def get_absolute_url(self):
        from accounts.views.user import SettingsView

        return reverse(SettingsView.get_view_name(), kwargs={"pk": self.pk})


class BoostedGroup(Group):
    active = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
    
    @property
    def users_count(self):
        return self.user_set.count()
    
    def get_group_users(self):
        return " | ".join([user.username for user in self.user_set.all()])
    
    def get_group_permissions(self):
        return " | ".join([perm.name for perm in self.permissions.all()])

    def delete(self, *args, **kwargs):
        if self.can_delete:
            super(BoostedGroup, self).delete(*args, **kwargs)
        raise ValueError("Cannot delete this model instance")