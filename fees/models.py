from django.db import models
from students.models import Student
from courses.models import Course


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_status = models.CharField(max_length=20, default='Pending')
    fee_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.fee_amount}"