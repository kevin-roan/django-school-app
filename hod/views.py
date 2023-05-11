from django.shortcuts import render
from hod.models import Hod

# Create your views here.
def admin(request):
     
    return render(request,'hod/hod.html')

