from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from datetime import datetime

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher_list.html", {"teachers": teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        joining_date = request.POST.get("joining_date")

        Teacher.objects.create(name=name, email=email, phone=phone, subject=subject, joining_date=joining_date)
        return redirect("teacher_list")

    return render(request, "teachers/add_teacher.html")

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        teacher.name = request.POST.get("name")
        teacher.email = request.POST.get("email")
        teacher.phone = request.POST.get("phone")
        teacher.subject = request.POST.get("subject")
        teacher.save()

        return redirect("teacher_list")

    return render(request, "teachers/edit_teacher.html", {"teacher": teacher})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect("teacher_list")
