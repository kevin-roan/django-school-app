from django.shortcuts import render
from django.http import HttpResponse

#
# def register(request):
#     return render(request, 'teacher/tchregister.html')
#

from register.models import Teacher
from register.models import Student
from register.models import Login

def register(request):
    if request.method=='POST':
        tch=Teacher()
        std=Student()
        if request.POST.get('teacher'):
            print("Teacher Login")
            tch.name = request.POST.get('username')
            tch.password = request.POST.get('userpass')
            tch.address = request.POST.get('useraddr')
            tch.phone = request.POST.get('userphone')
            tch.email = request.POST.get('usermail')
            tch.save()

            obj=Login()
            obj.username =  request.POST.get('username')
            obj.password =  request.POST.get('userpass')
            obj.type = "teacher"
            obj.u_id=tch.t_id
            obj.save()
            # checkuser("teacher")
        else:
            print("Student logged in ")
            std.name = request.POST.get('username')
            std.password = request.POST.get('userpass')
            std.address = request.POST.get('useraddr')
            std.phone = request.POST.get('userphone')
            std.email = request.POST.get('usermail')
            std.save()

            obj = Login()
            obj.username = request.POST.get('username')
            obj.password = request.POST.get('userpass')
            obj.type = "student"
            obj.u_id = std.std_id
            obj.save()
    return render(request, 'teacher/register.html')


