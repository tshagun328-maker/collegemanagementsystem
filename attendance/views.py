from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm


def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/attendance_list.html', {
        'attendances': attendances
    })


def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()

    return render(request, 'attendance/add_attendance.html', {
        'form': form
    })


def edit_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'attendance/edit_attendance.html', {
        'form': form,
        'attendance': attendance
    })


def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    attendance.delete()
    return redirect('attendance_list')