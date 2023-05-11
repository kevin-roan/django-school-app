from django.conf.urls import url
from teacher import views

urlpatterns= {
    # url('viewstudents/',views.view),
    # url('addstudents/', views.page),
    url('register/',views.register),
    url('managestudents/',views.managestudents),
    url('approve/(?P<idd>\w+)', views.approve),
    url('reject/(?P<idd>\w+)', views.reject),
    url('demo/', views.demo, name='demo'),
    url('notes/',views.notes)
}
