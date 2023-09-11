from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Users(AbstractUser):
    phone = models.CharField(unique=True, max_length=10, verbose_name='phone')

    class Meta:
        db_table = "t_user"
        verbose_name= 'UserTable'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
