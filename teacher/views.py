from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def register(request):
    return render(request, 'teacher/tchregister.html')


def addstudents(request):
    return render(request, 'teacher/addstudents.html')


from teacher.models import Student


def page(request):
    print("hellow")
    if request.method == 'POST':
        obj = Student()
        obj.studentname = request.POST.get('user')
        obj.studentphone = request.POST.get('phone')
        myfile = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.save()
    return render(request, 'teacher/addstudents.html')


def view(request):
    obj = Student.objects.all()
    context = {
        'kk': obj
    }
    return render(request, 'teacher/index.html', context)


def studentadd(request, idd):
    obj = Student.objects.get(login_id=idd)
    obj.username = "Kevin"
    obj.save()
    return view(request)


#
# def managestudents(request):
#     # obj= Student.objects.get(std_id=idd)
#     # obj.status = request.POST.get('')
#
#     return render(request,'teacher/managestudents.html')


def managestudents(request):
    obj=Student.objects.all()
    context={
        'kk':obj
    }

    return render(request,'teacher/managestudents.html',context)


def approve(request,idd):
    obj=Student.objects.get(std_id=idd)
    obj.status="approve"
    obj.save()
    return managestudents(request)


def reject(request,idd):
    obj=Student.objects.get(std_id=idd)
    obj.status="reject"
    obj.save()
    return managestudents(request)

from teacher.models import Notes
from django.core.files.storage import FileSystemStorage

def notes(request):
    if request.method == 'POST':
        obj=Notes()
        myfile=request.FILES["file"]
        fs=FileSystemStorage()
        obj.title=fs.save(myfile.name,myfile)
        obj.note = request.POST.get('notes')
        obj.save()
    return render(request,'teacher/notes.html')





## google calender api integration

from teacher.calendar_API import test_calendar

def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'teacher/demo.html', context)
