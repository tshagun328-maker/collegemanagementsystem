from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Student
from courses.models import Course

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

def add_student(request):

    courses = Course.objects.all()

    if request.method == "POST":

        name = request.POST.get("name")
        roll = request.POST.get("roll_no")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        address = request.POST.get("address")

        # course id lena
        course_id = request.POST.get("course")

        # database se actual course object lena
        selected_course = Course.objects.get(id=course_id)

        # student save karna
        Student.objects.create(
            name=name,
            roll_no=roll,
            email=email,
            phone=phone_no,
            address=address,
            course=selected_course
        )

        return redirect("student_list")

    return render(
        request,
        "students/add_student.html",
        {
            "courses": courses
        }
    )


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_no = request.POST.get("roll_no")
        student.course = request.POST.get("course")
        student.email = request.POST.get("email")
        student.phone_no = request.POST.get("phone_no")
        student.address = request.POST.get("address")
        student
        student.save()
        return redirect("student_list")

    return render(request, "students/student_edit.html", {"student": student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")

def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')