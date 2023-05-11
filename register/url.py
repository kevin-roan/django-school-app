from django.conf.urls import url
from register import views

urlpatterns= [
    url('', views.register),
]


