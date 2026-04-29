from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Roles=[('admin','ADMIN'),
           ('teacher','TEACHER'),
           ('student','STUDENT')
           ]
    role=models.CharField(max_length=50,choices=Roles)
