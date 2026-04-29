from django.db import models
from django.conf import settings


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    roll_number = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    assigned_teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_students',
        limit_choices_to={'role': 'teacher'}
    )

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"