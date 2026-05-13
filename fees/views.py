# fees/views.py

from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from .models import Fee


# Fee List
def fee_list(request):
    fees = Fee.objects.all()
    return render(request, "fees/fee_list.html", {
        "fees": fees
    })


# Add Fee
def add_fee(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student")
        amount = request.POST.get("amount")
        status = request.POST.get("status")
        date = request.POST.get("date")

        selected_student = Student.objects.get(id=student_id)

        Fee.objects.create(
            student=selected_student,
            fee_amount=amount,
            fee_status=status,
            fee_date=date
        )

        return redirect("fee_list")

    return render(request, "fees/add_fee.html", {
        "students": students
    })


# Edit Fee
def edit_fee(request, id):
    fee = get_object_or_404(Fee, id=id)
    students = Student.objects.all()

    if request.method == "POST":
        fee.student = Student.objects.get(id=request.POST.get("student"))
        fee.amount = request.POST.get("amount")
        fee.status = request.POST.get("status")
        fee.date = request.POST.get("date")
        fee.save()

        return redirect("fee_list")

    return render(request, "fees/edit_fee.html", {
        "fee": fee,
        "students": students
    })


# Delete Fee
def delete_fee(request, id):
    fee = get_object_or_404(Fee, id=id)
    fee.delete()
    return redirect("fee_list")


