from django.contrib.auth.backends import ModelBackend


class BoostedAuthenticationBackend(ModelBackend):
    def user_can_authenticate(self, user):
        return True
