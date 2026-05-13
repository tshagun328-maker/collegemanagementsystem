from django.shortcuts import render, redirect
from .models import Course

# List
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# Add
def add_course(request):
    if request.method == "POST":
        name = request.POST.get("name")

        Course.objects.create(name=name)

        return redirect('course_list')

    return render(request, 'courses/add_course.html')


# Delete
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course_list')