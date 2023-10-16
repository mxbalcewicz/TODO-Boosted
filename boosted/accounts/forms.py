from accounts.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = ("username", "email")
        labels = {
            "email": "Email",
            "username": "Username",
        }

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user


class UserSettingsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Change password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = "__all__"
        exclude = ("is_admin", "is_superuser", "last_login")
        labels = {
            "is_active": "Account active",
        }

    def __init__(self, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        for field in ("avatar", "password", "password2"):
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super(UserSettingsForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match.")

        # Remove fields with empty values from cleaned_data
        for field in self.fields:
            if (
                field in ("password", "password2", "avatar")
                and cleaned_data.get(field) == ""
            ):
                del cleaned_data[field]
        return cleaned_data
