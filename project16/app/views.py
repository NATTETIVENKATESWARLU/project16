from django.shortcuts import render

# Create your views here.
from app.models import *
def venkey(request):
    l=Topic.objects.all()
    d={'l':l}
    return render(request,'venkey.html',d)

def mass(request):
    l=webpages.objects.all()
    d={'l':l}
    return render(request,'mass.html',d)

def mass1(request):
    l=A_R.objects.all()
    d={'l':l}
    return render(request,'mass1.html',d)

