from django.shortcuts import render
from .models import *

def home(request):
    return render(request, "dashbord.html")

def fakultetView(request):
    return render(request, "fakultet.html")

def maglumatView(request):
    return render(request, "maglumat.html")

def dashbordView(request):
    return render(request, "dashbord.html")

def bizView(request):
    return render(request, "biz.html")

def tazeView(request):
    return render(request, "taze.html")

def yasView(request):
    return render(request, "yas.html")

def t1View(request):
    return render(request, "t1.html")

def t2View(request):
    return render(request, "t2.html")

def t3View(request):
    return render(request, "t3.html")

def tazelikView(request):
    tazelikView = Continet.objects.all()
    return render(request, "tazelik.html", {'tazelikView':tazelikView})


# Create your views here.
