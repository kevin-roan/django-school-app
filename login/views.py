from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# def login(request):
#     return render(request, 'login/login.html')
# Create your views here.
#
# from login.models import Teacherlogin
# from login.models import Studentlogin

# def checkuser(user):
#     if user=="teacher":
#     tch=Teacherlogin.objects.all()
#     context = {
#         'kk': tch
#     }
#     for i in kk:
#
#     else:
#     std=Studentlogin.objects.all()
#     context={
#         'kk':std
#     }
#     print(context)
#     return HttpResponse("User Check Valid")
#
# def checkuser(user):
#     if user=="teacher":
#         print("Teacher Logged In")
#         tch=Teacherlogin.objects.all()
#         context={
#             'kk':tch
#         }
#     return HttpResponse("Teacher Logged In")

from login.models import Teacher
from login.models import Student

# def login(request):
#     if request.method=='POST':
#         if request.POST.get('teacher'):
#             print("Teacher Logined in ")
#             obj = Teacher.objects.all()
#             for i in Teacher.objects.all():
#               if request.POST.get('teachername') == i.name and request.POST.get('teacherpass') == i.password:
#                   print("Teacher FOund ")
#                   return render(request, 'teacher/managestudents.html')
#               else:
#                   print("User Not Found")
#         else:
#             print("Student Logined In")
#     return render(request,'login/teacherlogin.html')

from login.models import Login

def login(request):
    if request.method=='POST':
        tchname = request.POST.get('username')
        tchpass = request.POST.get('userpass')
        obj = Login.objects.filter(username=tchname,password=tchpass)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "teacher":
                request.session["uid"] = uid
                return HttpResponseRedirect('/teacher/managestudents')
            elif tp == "student":
                request.session["uid"] = uid
                return HttpResponseRedirect('/student/notes')

        else:
            objlist = "Username or Password incorrect..."
            context={
                'mag' : objlist,
            }
            return render(request,'login/teacherlogin.html',context)
        return render(request,'login/teacherlogin.html')
    return render(request,'login/teacherlogin.html')


def logout(request):
    print("log out success")
    return render(request,'teacher/notes.html')