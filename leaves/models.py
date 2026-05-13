from django.db import models
from students.models import Student

class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.student.user.username} - {self.status}"


# Create your models here.
