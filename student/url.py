from django.conf.urls import url
from student import views


urlpatterns = {
    # url('',views.studentview),
    url('teacherlist/',views.studentview),
    url('notes',views.viewnotes)
}