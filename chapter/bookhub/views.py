from django.shortcuts import render
from django.contrib import messages

def index(request):
    
    return render(request,"index.html")

def base(request):
    return render(request,"base.html")
   

def coming(request):
    return render(request,'coming.html')

