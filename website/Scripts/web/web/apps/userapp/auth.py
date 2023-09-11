import re

from django.contrib.auth.backends import ModelBackend
from  userapp.models import Users


class MultiAccountLogin(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if re.match(r'^[2-9][0-9]{2}[2-9][0-9]{2}[0-9]{4}$', username):
                user = Users.objects.get(phone=username)
            elif re.match(r'^([0-9a-zA-Z_-])+@([a-zA-Z0-p_-])+(.[a-zA-Z0-9_-])+', username):
                user = Users.objects.get(email=username)
            else:
                user = Users.objects.get(username=username)

        except Users.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user
