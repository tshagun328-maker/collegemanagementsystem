from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from datetime import date


def notice_list(request):
    notices = Notice.objects.all().order_by('-id')
    return render(request, 'notices/notice_list.html', {'notices': notices})


def add_notice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Notice.objects.create(
            title=title,
            description=description,
            date=date.today()
        )

        return redirect('notice_list')

    return render(request, 'notices/add_notice.html')


def delete_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('notice_list')


def edit_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)

    if request.method == 'POST':
        notice.title = request.POST.get('title')
        notice.description = request.POST.get('description')
        notice.save()
        return redirect('notice_list')

    return render(request, 'notices/add_notice.html', {'notice': notice})