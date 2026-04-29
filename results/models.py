from django.db import models
from students.models import Student


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    total_marks = models.IntegerField(default=100)

    class Meta:
        unique_together = ('student', 'subject')

    @property
    def subject_status(self):
        return "Fail" if self.marks < 35 else "Pass"

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject}"