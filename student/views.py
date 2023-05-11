from django.shortcuts import render
from django.http import HttpResponse

from student.models import Teacher
from student.models import Notes


def studentview(request):
    obj = Teacher.objects.all()
    context = {
        'kk': obj
    }
    return render(request, 'teacher/viewteachers.html', context)


# noti = Notes.objects.filter()
# context = {
#     'notes': noti
# }
# return render(request,'teacher/viewteachers.html',context)

#
from student.models import Notes


def viewnotes(request):
    obj = Notes.objects.filter()
    context = {
        'notes': obj
    }
    return render(request, 'teacher/notesview.html', context)
