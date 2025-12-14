from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .user_manager import UserManager




class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=20,null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    phone = models.CharField(null=True,unique=True,max_length=15)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.BigIntegerField(null=True)
    updated_by = models.BigIntegerField(null=True)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
