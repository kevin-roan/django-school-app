from django.conf.urls import url
from login import views

urlpatterns= [
    url('', views.login),
    # url('logout/',views.logout),
]


