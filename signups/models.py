from django.db import models


class SignUp(models.Model):
    email = models.EmailField(unique=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
