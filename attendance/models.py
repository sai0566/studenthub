from django.db import models
from students.models import Student
from datetime import date

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')  # prevent duplicate same-day entry

    def __str__(self):
        return f"{self.student.roll_number} - {self.date} - {self.status}"