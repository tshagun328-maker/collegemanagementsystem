# exams/views.py
# Is code ko pura replace kar do.
# Ye code Exam Type, Max Marks aur Percentage ko automatically save karega.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from students.models import Student
from courses.models import Course


# =========================
# Exam List
# =========================
def exam_list(request):
    exams = Exam.objects.select_related('student', 'course').all()
    return render(request, 'exams/exam_list.html', {'exams': exams})


# =========================
# Add Exam
# =========================
def add_exam(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        student = Student.objects.get(id=request.POST.get('student'))
        course = Course.objects.get(id=request.POST.get('course'))

        exam_type = request.POST.get('exam_type')
        marks = float(request.POST.get('marks') or 0)
        max_marks = float(request.POST.get('max_marks') or 0)
        date = request.POST.get('date')

        # Percentage calculation
        if max_marks > 0:
            percentage = (marks / max_marks) * 100
        else:
            percentage = 0

        Exam.objects.create(
            student=student,
            course=course,
            exam_type=exam_type,
            marks=marks,
            max_marks=max_marks,
            percentage=round(percentage, 2),
            date=date
        )

        return redirect('exam_list')

    return render(request, 'exams/add_exam.html', {
        'students': students,
        'courses': courses
    })


# =========================
# Edit Exam
# =========================
def edit_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        exam.student = Student.objects.get(id=request.POST.get('student'))
        exam.course = Course.objects.get(id=request.POST.get('course'))

        exam.exam_type = request.POST.get('exam_type')
        exam.marks = float(request.POST.get('marks') or 0)
        exam.max_marks = float(request.POST.get('max_marks') or 0)
        exam.date = request.POST.get('date')

        # Percentage calculation
        if exam.max_marks > 0:
            exam.percentage = round((exam.marks / exam.max_marks) * 100, 2)
        else:
            exam.percentage = 0

        exam.save()
        return redirect('exam_list')

    return render(request, 'exams/add_exam.html', {
        'exam': exam,
        'students': students,
        'courses': courses
    })


# =========================
# Delete Exam
# =========================
def delete_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    exam.delete()
    return redirect('exam_list')