from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable
from courses.models import Course


def timetable_list(request):
    timetables = Timetable.objects.select_related('course').all().order_by('id')
    return render(request, 'timetable_list.html', {
        'timetables': timetables
    })


def add_timetable(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        Timetable.objects.create(
            course=Course.objects.get(id=request.POST.get('course')),
            subject=request.POST.get('subject'),
            day=request.POST.get('day'),
            year=request.POST.get('year'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            room=request.POST.get('room')
        )
        return redirect('timetable_list')

    return render(request, 'add_timetable.html', {
        'courses': courses
    })


def edit_timetable(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    courses = Course.objects.all()

    if request.method == 'POST':
        timetable.course = Course.objects.get(id=request.POST.get('course'))
        timetable.subject = request.POST.get('subject')
        timetable.day = request.POST.get('day')
        timetable.year = request.POST.get('year')
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')
        timetable.room = request.POST.get('room')
        timetable.save()
        return redirect('timetable_list')

    return render(request, 'add_timetable.html', {
        'timetable': timetable,
        'courses': courses
    })


def delete_timetable(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    timetable.delete()
    return redirect('timetable_list')