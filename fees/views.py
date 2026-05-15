# fees/views.py
# Total Amount + Paid Amount user enter karega
# Pending Amount automatically calculate hoga:
# pending_amount = total_amount - paid_amount

from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from students.models import Student
from courses.models import Course


# =========================
# Fee List
# =========================
def fee_list(request):
    fees = Fee.objects.all().order_by('-id')
    return render(request, 'fees/fee_list.html', {
        'fees': fees
    })


# =========================
# Add Fee
# =========================
def add_fee(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        student = Student.objects.get(id=request.POST.get('student'))
        course = Course.objects.get(id=request.POST.get('course'))

        total_amount = float(request.POST.get('total_amount') or 0)
        paid_amount = float(request.POST.get('paid_amount') or 0)

        # Automatic calculation
        pending_amount = total_amount - paid_amount

        # Negative value avoid
        if pending_amount < 0:
            pending_amount = 0

        status = request.POST.get('status')
        date = request.POST.get('date')

        Fee.objects.create(
            student=student,
            course=course,
            total_amount=total_amount,
            paid_amount=paid_amount,
            pending_amount=pending_amount,
            status=status,
            date=date
        )

        return redirect('fee_list')

    return render(request, 'fees/add_fee.html', {
        'students': students,
        'courses': courses
    })


# =========================
# Edit Fee
# =========================
def edit_fee(request, id):
    fee = get_object_or_404(Fee, id=id)
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        fee.student = Student.objects.get(id=request.POST.get('student'))
        fee.course = Course.objects.get(id=request.POST.get('course'))

        fee.total_amount = float(request.POST.get('total_amount') or 0)
        fee.paid_amount = float(request.POST.get('paid_amount') or 0)

        # Automatic calculation
        fee.pending_amount = fee.total_amount - fee.paid_amount

        # Negative value avoid
        if fee.pending_amount < 0:
            fee.pending_amount = 0

        fee.status = request.POST.get('status')
        fee.date = request.POST.get('date')

        fee.save()
        return redirect('fee_list')

    return render(request, 'fees/add_fee.html', {
        'fee': fee,
        'students': students,
        'courses': courses
    })


# =========================
# Delete Fee
# =========================
def delete_fee(request, id):
    fee = get_object_or_404(Fee, id=id)
    fee.delete()
    return redirect('fee_list')